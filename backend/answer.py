"""5단계: 답변 생성하기 (RAG 완성)

질문 → 검색(4단계) → 점수 기준 통과한 조각만 골라서 → LLM이 그 조각만 근거로 답한다.
근거가 없으면 LLM을 부르지 않고 "모른다"고 답한다.
실행:
  python answer.py "질문"
  python answer.py             # 대화형 (빈 줄 입력 시 종료)
"""

import sys

import ollama

from search import search

CHAT_MODEL = "gemma3:4b"
# Ollama 기본값(약 2,000토큰)이면 조각 4개 + 답변이 넘칠 수 있다
NUM_CTX = 8192
TOP_K = 4
# 4단계 실험: 관련 조각 0.55~0.69 / 무관한 조각 ~0.33 / 애매한 질문 0.46~0.49
MIN_SCORE = 0.5
# 1위보다 이만큼 이상 낮은 조각은 뺀다. 관련 없는 조각이 섞이면 작은 모델(4B)이 헷갈려서
# 정답 조각이 있어도 "모른다"고 답하는 문제가 있었다 (예: pip 질문에 npm 조각이 섞임)
SCORE_MARGIN = 0.08

NO_ANSWER = "문서에서 관련 내용을 찾지 못했습니다."

PROMPT_TEMPLATE = """너는 사용자가 올린 문서를 근거로 답하는 도우미야.
아래 [자료]에 있는 내용만 사용해서 [질문]에 한국어로 답해.

규칙:
- [자료]에 없는 내용은 추측하거나 지어내지 마.
- [자료]만으로 답할 수 없으면 정확히 "{no_answer}"라고만 답해.
- 명령어나 코드는 자료에 있는 그대로 코드 블록으로 보여줘.

[자료]
{context}

[질문]
{question}
"""


def build_context(hits: list[dict]) -> str:
    blocks = []
    for number, hit in enumerate(hits, start=1):
        blocks.append(f"<자료 {number}> 출처: {hit['source']} > {hit['heading']}\n{hit['text']}")
    return "\n\n".join(blocks)


def answer(question: str, source: str | None = None) -> dict:
    hits = search(question, top_k=TOP_K, source=source)
    best_score = max((hit["score"] for hit in hits), default=0)
    relevant = [
        hit
        for hit in hits
        if hit["score"] >= MIN_SCORE and hit["score"] >= best_score - SCORE_MARGIN
    ]

    if not relevant:
        # 근거가 없으면 LLM을 부르지 않는다 → 지어낼 기회 자체를 없앤다
        return {"answer": NO_ANSWER, "sources": [], "hits": hits}

    prompt = PROMPT_TEMPLATE.format(
        no_answer=NO_ANSWER,
        context=build_context(relevant),
        question=question,
    )
    response = ollama.chat(
        model=CHAT_MODEL,
        messages=[{"role": "user", "content": prompt}],
        options={"temperature": 0, "num_ctx": NUM_CTX},  # 근거 기반 답변은 창의성보다 일관성이 중요하다
    )
    return {
        "answer": response["message"]["content"].strip(),
        "sources": relevant,
        "hits": hits,
    }


def print_answer(question: str, result: dict) -> None:
    print(f"\n질문: {question}")
    print(f"\n{result['answer']}\n")
    if result["sources"]:
        print("출처:")
        for hit in result["sources"]:
            print(f"  - {hit['source']} > {hit['heading']} (유사도 {hit['score']:.3f})")
    else:
        best = max((hit["score"] for hit in result["hits"]), default=0)
        print(f"(가장 가까운 조각 유사도 {best:.3f} < 기준 {MIN_SCORE})")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        question = " ".join(sys.argv[1:])
        print_answer(question, answer(question))
    else:
        while question := input("\n질문 (종료: 엔터) > ").strip():
            print_answer(question, answer(question))
