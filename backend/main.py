from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from summarize import summarize

app = FastAPI(title="Ollama Doc Assistant")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
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