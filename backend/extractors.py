"""업로드한 파일에서 텍스트를 뽑는다. 형식이 늘어나면(엑셀 등) 여기에 추가한다."""

from io import BytesIO
from pathlib import PurePath

from pypdf import PdfReader

SUPPORTED_EXTENSIONS = {".md", ".txt", ".pdf"}


class ExtractError(ValueError):
    """사용자에게 그대로 보여 줄 수 있는 추출 실패 이유"""


def extract_text(filename: str, data: bytes) -> str:
    ext = PurePath(filename).suffix.lower()

    if ext in {".md", ".txt"}:
        try:
            return data.decode("utf-8")
        except UnicodeDecodeError:
            raise ExtractError("UTF-8 텍스트 파일만 읽을 수 있습니다.")

    if ext == ".pdf":
        return extract_pdf(data)

    raise ExtractError(f"지원하지 않는 형식입니다: {ext or '확장자 없음'}")


def extract_pdf(data: bytes) -> str:
    try:
        reader = PdfReader(BytesIO(data))
    except Exception:
        raise ExtractError("PDF 파일을 열 수 없습니다.")

    pages = []
    for number, page in enumerate(reader.pages, start=1):
        text = (page.extract_text() or "").strip()
        if text:
            pages.append(f"## p.{number}\n{text}")

    if not pages:
        raise ExtractError("PDF에서 텍스트를 찾지 못했습니다. 스캔한 이미지 PDF일 수 있어요.")

    return "\n\n".join(pages)
