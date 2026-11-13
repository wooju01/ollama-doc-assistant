import unicodedata
from pathlib import PurePath

from fastapi import FastAPI, HTTPException, UploadFile
from fastapi.concurrency import run_in_threadpool
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from answer import answer
from extractors import SUPPORTED_EXTENSIONS, ExtractError, extract_text
from ingest import get_collection, ingest_text
from summarize import summarize

MAX_UPLOAD_BYTES = 20 * 1024 * 1024  


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
    text:str


@app.post("/api/v1/documents", response_model=DocumentResponse)
async def upload_document(file: UploadFile):
    """업로드한 파일에서 텍스트를 뽑고, 조각내고 임베딩해서 벡터 DB에 저장한다 (같은 이름이면 덮어쓴다)."""
    # 경로가 섞여 와도 파일명만 쓰고, 한글 자모 분리형(NFD)은 합친다(NFC)
    filename = unicodedata.normalize("NFC", PurePath(file.filename or "").name)
    if PurePath(filename).suffix.lower() not in SUPPORTED_EXTENSIONS:
        raise HTTPException(status_code=415, detail="지금은 .md, .txt, .pdf 파일만 지원합니다.")

    data = await file.read(MAX_UPLOAD_BYTES + 1)
    if len(data) > MAX_UPLOAD_BYTES:
        raise HTTPException(status_code=413, detail="파일이 너무 큽니다. (최대 20MB)")

    try:
        # PDF 추출은 시간이 걸릴 수 있어서 스레드에서 돌린다
        text = await run_in_threadpool(extract_text, filename, data)
    except ExtractError as error:
        raise HTTPException(status_code=422, detail=str(error))

    if not text.strip():
        raise HTTPException(status_code=422, detail="파일 내용이 비어 있습니다.")

    # 임베딩은 몇 초 걸리는 동기 작업이라, 그동안 다른 요청(요약 등)이 막히지 않게 스레드에서 돌린다
    chunks = await run_in_threadpool(ingest_text, get_collection(), text, filename)
    return {"source": filename, "chunks": chunks, "text": text}



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
