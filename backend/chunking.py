

import re
from dataclasses import dataclass

CHUNK_SIZE = 800
CHUNK_OVERLAP = 100
# 제목을 뺀 본문이 이보다 짧은 섹션은 다음 섹션과 합친다.
# 예: "# 42. 오류 해결" 처럼 제목만 있는 조각은 내용이 없어서 검색 잡음이 된다.
MIN_BODY_CHARS = 30


@dataclass
class Chunk:
    id: str 
    text: str
    source: str
    index: int
    heading: str


HEADING_RE = re.compile(r"^#{1,3} ")
DIVIDER_RE = re.compile(r"^-{3,}\s*$")


def split_by_heading(text: str) -> list[str]:
    """제목(#, ##, ###) 줄마다 새 섹션을 시작한다.
    단, 코드 블록(```) 안의 '# 주석'이나 '### main.py' 같은 줄은 제목이 아니므로 무시한다."""
    sections: list[list[str]] = [[]]
    in_code = False

    for line in text.splitlines():
        if line.lstrip().startswith("```"):
            in_code = not in_code
        elif not in_code:
            if DIVIDER_RE.match(line):  # 구분선(---)은 의미가 없으니 제거
                continue
            if HEADING_RE.match(line):
                sections.append([])
        sections[-1].append(line)

    parts = ("\n".join(lines).strip() for lines in sections)
    return [part for part in parts if part]


def get_heading(section: str) -> str:
    first_line = section.splitlines()[0]
    return first_line.lstrip("#").strip() if first_line.startswith("#") else ""


def body_length(section: str) -> int:
    """제목 줄을 뺀 본문 글자 수"""
    lines = section.splitlines()
    body = lines[1:] if lines and lines[0].startswith("#") else lines
    return len("".join(body).strip())


def merge_short_sections(sections: list[str]) -> list[tuple[str, str]]:
    """본문이 짧은 섹션은 다음 섹션 앞에 붙인다. (섹션 내용, 합쳐진 제목) 목록을 돌려준다.
    합쳐진 제목은 "42. 오류 해결 > 오류 1"처럼 이어 붙여서 상위 맥락도 남긴다."""
    merged: list[tuple[str, str]] = []
    pending_text: list[str] = []
    pending_headings: list[str] = []

    for section in sections:
        pending_text.append(section)
        if heading := get_heading(section):
            pending_headings.append(heading)

        if body_length(section) >= MIN_BODY_CHARS:
            merged.append(("\n\n".join(pending_text), " > ".join(pending_headings)))
            pending_text, pending_headings = [], []

    if pending_text:  # 문서 끝에 짧은 섹션이 남으면 바로 앞 섹션에 붙인다
        if merged:
            last_text, last_heading = merged.pop()
            merged.append(("\n\n".join([last_text, *pending_text]), last_heading))
        else:
            merged.append(("\n\n".join(pending_text), " > ".join(pending_headings)))

    return merged


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

    for section, heading in merge_short_sections(split_by_heading(text)):
        if len(section) <= size:
            pieces = [section]
        else:
            pieces = split_by_size(section, size, overlap)
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
