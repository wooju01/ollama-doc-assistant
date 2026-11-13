
import sys

from ingest import embed, get_collection

TOP_K = 3


def search(question: str, top_k: int = TOP_K) -> list[dict]:
    collection = get_collection()
    result = collection.query(
        query_embeddings=embed([question]),  
        n_results=top_k,
        include=["documents", "metadatas", "distances"],
    )

    hits = []
    for chunk_id, document, metadata, distance in zip(
        result["ids"][0],
        result["documents"][0],
        result["metadatas"][0],
        result["distances"][0],
    ):
        hits.append(
            {
                "id": chunk_id,
                "text": document,
                "source": metadata["source"],
                "heading": metadata["heading"],
                # chromadb는 '거리'(작을수록 가까움)를 준다. 코사인 거리 = 1 - 코사인 유사도
                "score": 1 - distance,
            }
        )
    return hits


def print_hits(question: str, hits: list[dict]) -> None:
    print(f"\n질문: {question}")
    for rank, hit in enumerate(hits, start=1):
        preview = hit["text"][:120].replace("\n", " ")
        print(f"  {rank}위  유사도 {hit['score']:.3f}  [{hit['source']} > {hit['heading']}]")
        print(f"       {preview}...")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        question = " ".join(sys.argv[1:])
        print_hits(question, search(question))
    else:
        while question := input("\n질문 (종료: 엔터) > ").strip():
            print_hits(question, search(question))
