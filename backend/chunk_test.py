"""2단계: 문서 조각내기 (Chunking)

방법 A: 글자 수 기준으로 자르기 (겹침 포함)
방법 B: 마크다운 제목(##) 기준으로 자르기
실행: python chunk_test.py
"""

import re
from pathlib import Path

DOCS_DIR = Path(__file__).parent / "docs"


def chunk_by_size(text: str, size: int = 200, overlap: int = 50) -> list[str]:
    """size 글자씩 자르되, 앞 조각의 끝 overlap 글자를 다음 조각 앞에 겹쳐 넣는다.
    겹침이 있어야 문장이 경계에서 잘려도 앞뒤 맥락이 한 조각에 남는다."""
    if overlap >= size:
        raise ValueError("overlap은 size보다 작아야 합니다")

    chunks = []
    start = 0
    while start < len(text):
        chunk = text[start : start + size].strip()
        if chunk:
            chunks.append(chunk)
        if start + size >= len(text):
            break
        start += size - overlap
    return chunks


def chunk_by_heading(text: str) -> list[str]:
    """'## 제목' 줄이 나올 때마다 새 조각을 시작한다. 제목이 조각 안에 함께 들어간다."""
    parts = re.split(r"(?m)^(?=#{1,3} )", text)
    return [part.strip() for part in parts if part.strip()]


def show(title: str, chunks: list[str], source: str) -> None:
    print(f"===== {title}: {len(chunks)}개 =====")
    for index, chunk in enumerate(chunks):
        print(f"--- [{source} #{index}] {len(chunk)}자 ---")
        print(chunk)
        print()


if __name__ == "__main__":
    for path in sorted(DOCS_DIR.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        print(f"### 파일: {path.name} ({len(text)}자)\n")
        show("방법 A: 글자 수 (200자, 겹침 50자)", chunk_by_size(text), path.name)
        show("방법 B: 제목 기준", chunk_by_heading(text), path.name)
