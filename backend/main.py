from pathlib import PurePath

from fastapi import FastAPI, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from answer import answer
from ingest import get_collection, ingest_text
from summarize import summarize

ALLOWED_EXTENSIONS = {".md", ".txt"}
MAX_UPLOAD_BYTES = 2 * 1024 * 1024  # 2MB

app = FastAPI(title="Ollama Doc Assistant")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:5174"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class SummaryRequest(BaseModel):
    text: str = Field(min_length=1)


class SummaryResponse(BaseModel):
    summary: str


@app.post("/api/v1/summaries", response_model=SummaryResponse)
def create_summary(body: SummaryRequest):
    result = summarize(body.text)
    return {"summary": result}


class DocumentResponse(BaseModel):
    source: str
    chunks: int


@app.post("/api/v1/documents", response_model=DocumentResponse)
async def upload_document(file: UploadFile):
    """업로드한 파일을 조각내고 임베딩해서 벡터 DB에 저장한다 (같은 이름이면 덮어쓴다)."""
    filename = PurePath(file.filename or "").name  # 경로가 섞여 와도 파일명만 쓴다
    if PurePath(filename).suffix.lower() not in ALLOWED_EXTENSIONS:
        raise HTTPException(status_code=415, detail="지금은 .md, .txt 파일만 지원합니다.")

    data = await file.read(MAX_UPLOAD_BYTES + 1)
    if len(data) > MAX_UPLOAD_BYTES:
        raise HTTPException(status_code=413, detail="파일이 너무 큽니다. (최대 2MB)")

    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError:
        raise HTTPException(status_code=422, detail="UTF-8 텍스트 파일만 읽을 수 있습니다.")

    if not text.strip():
        raise HTTPException(status_code=422, detail="파일 내용이 비어 있습니다.")

    chunks = ingest_text(get_collection(), text, source=filename)
    return {"source": filename, "chunks": chunks}


class QuestionRequest(BaseModel):
    question: str = Field(min_length=1, max_length=500)
    # 값이 있으면 그 문서에서만 찾는다 (업로드한 문서에 질문할 때)
    source: str | None = None


class Source(BaseModel):
    source: str
    heading: str
    score: float
    text: str


class QuestionResponse(BaseModel):
    answer: str
    sources: list[Source]


@app.post("/api/v1/questions", response_model=QuestionResponse)
def create_answer(body: QuestionRequest):
    result = answer(body.question.strip(), source=body.source)
    return {
        "answer": result["answer"],
        "sources": [
            {
                "source": hit["source"],
                "heading": hit["heading"],
                "score": round(hit["score"], 3),
                "text": hit["text"],
            }
            for hit in result["sources"]
        ],
    }
