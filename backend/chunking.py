"""문서 조각내기 (2단계 결과물)

1. 마크다운 제목(#, ##, ###) 기준으로 의미 단위를 나눈다.
2. 너무 긴 섹션만 글자 수 기준으로 다시 자른다 (겹침 포함).
3. 잘게 나뉜 조각에도 섹션 제목을 붙여서, 무엇에 대한 내용인지 벡터에 남긴다.
"""

import re
from dataclasses import dataclass

CHUNK_SIZE = 800
CHUNK_OVERLAP = 100


@dataclass
class Chunk:
    id: str  # "파일명#순번" — 다시 색인해도 같은 id라 중복 저장되지 않는다
    text: str
    source: str
    index: int
    heading: str


def split_by_heading(text: str) -> list[str]:
    parts = re.split(r"(?m)^(?=#{1,3} )", text)
    return [part.strip() for part in parts if part.strip()]


def split_by_size(text: str, size: int, overlap: int) -> list[str]:
    if overlap >= size:
        raise ValueError("overlap은 size보다 작아야 합니다")

    pieces = []
    start = 0
    while start < len(text):
        piece = text[start : start + size].strip()
        if piece:
            pieces.append(piece)
        if start + size >= len(text):
            break
        start += size - overlap
    return pieces


def chunk_document(
    text: str,
    source: str,
    size: int = CHUNK_SIZE,
    overlap: int = CHUNK_OVERLAP,
) -> list[Chunk]:
    chunks: list[Chunk] = []

    for section in split_by_heading(text):
        first_line = section.splitlines()[0]
        heading = first_line.lstrip("#").strip() if first_line.startswith("#") else ""

        if len(section) <= size:
            pieces = [section]
        else:
            pieces = split_by_size(section, size, overlap)
            # 두 번째 조각부터는 제목이 잘려 나갔으니 앞에 다시 붙여 준다
            pieces = [pieces[0]] + [f"## {heading}\n{p}" if heading else p for p in pieces[1:]]

        for piece in pieces:
            index = len(chunks)
            chunks.append(
                Chunk(
                    id=f"{source}#{index}",
                    text=piece,
                    source=source,
                    index=index,
                    heading=heading,
                )
            )

    return chunks
