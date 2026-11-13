from pathlib import Path
import ollama

MODEL = "gemma3:4b"


def summarize(text: str) -> str:
    prompt = f"""아래 문서를 한국어로 요약해줘.
- 핵심 내용을 3~5개 bullet로
- 마지막에 한 줄 요약 추가

[문서]
{text}
"""
    response = ollama.chat(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
    )
    return response["message"]["content"]


if __name__ == "__main__":
    doc_path = Path(__file__).parent / "docs" / "Python 가상환경 설치.md"
    text = doc_path.read_text(encoding="utf-8")
    print(summarize(text))