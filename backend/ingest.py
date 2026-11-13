"""3단계: 벡터 DB에 저장하기 (색인)

docs/ 폴더의 문서를 읽어서 → 조각내고 → bge-m3로 임베딩해서 → chromadb에 저장한다.
여러 번 실행해도 같은 조각이 중복 저장되지 않는다.
실행: python ingest.py
"""

from pathlib import Path

import chromadb
import ollama

from chunking import chunk_document

BASE_DIR = Path(__file__).parent
DOCS_DIR = BASE_DIR / "docs"
DB_DIR = BASE_DIR / "chroma_db"

EMBED_MODEL = "bge-m3"
COLLECTION_NAME = "docs"


def get_collection() -> chromadb.Collection:
    client = chromadb.PersistentClient(path=str(DB_DIR))  
    return client.get_or_create_collection(
        name=COLLECTION_NAME,
        metadata={"hnsw:space": "cosine"},  
    )


def embed(texts: list[str]) -> list[list[float]]:
    return ollama.embed(model=EMBED_MODEL, input=texts)["embeddings"]


def ingest_file(collection: chromadb.Collection, path: Path) -> int:
    return ingest_text(collection, path.read_text(encoding="utf-8"), source=path.name)


def ingest_text(collection: chromadb.Collection, text: str, source: str) -> int:
    """텍스트를 조각내고 임베딩해서 저장한다. 웹 업로드(main.py)에서도 이 함수를 쓴다."""
    chunks = chunk_document(text, source=source)

    # 문서가 수정되어 조각 수가 줄었을 수도 있으니, 이 문서의 예전 조각을 먼저 지운다
    collection.delete(where={"source": source})
    if not chunks:
        return 0

    collection.upsert(
        ids=[chunk.id for chunk in chunks],
        documents=[chunk.text for chunk in chunks],
        embeddings=embed([chunk.text for chunk in chunks]),
        metadatas=[
            {"source": chunk.source, "index": chunk.index, "heading": chunk.heading}
            for chunk in chunks
        ],
    )
    return len(chunks)


if __name__ == "__main__":
    collection = get_collection()

    paths = sorted(list(DOCS_DIR.glob("*.md")) + list(DOCS_DIR.glob("*.txt")))
    for path in paths:
        count = ingest_file(collection, path)
        print(f"{path.name}: 조각 {count}개 저장")

    print(f"\n컬렉션 '{COLLECTION_NAME}' 전체 조각 수: {collection.count()}")

    # 저장된 내용 확인 (앞 3개)
    stored = collection.get(limit=3, include=["documents", "metadatas", "embeddings"])
    for chunk_id, document, metadata, vector in zip(
        stored["ids"], stored["documents"], stored["metadatas"], stored["embeddings"]
    ):
        preview = document[:60].replace("\n", " ")
        print(f"- {chunk_id} | 제목: {metadata['heading']} | 벡터 {len(vector)}차원 | {preview}...")
