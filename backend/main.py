from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from answer import answer
from summarize import summarize

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


class QuestionRequest(BaseModel):
    question: str = Field(min_length=1, max_length=500)


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
    result = answer(body.question.strip())
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
