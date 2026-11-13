"""1단계: 임베딩 이해하기 + 모델 비교

문장을 벡터(숫자 목록)로 바꾸고, 문장끼리 얼마나 비슷한지 코사인 유사도로 비교한다.
여러 임베딩 모델로 같은 실험을 해서 어떤 모델이 한국어 의미를 잘 구분하는지 본다.
실행: python embed_test.py
"""

import math
import time

import ollama

MODELS = ["nomic-embed-text", "bge-m3"]

# (문장, 주제) — 같은 주제끼리는 가깝고, 다른 주제와는 멀어야 좋은 모델
sentences = [
    ("파이썬 설치하는 방법을 알려줘", "파이썬"),
    ("가상환경은 python -m venv 명령으로 만든다", "파이썬"),
    ("오늘 날씨가 맑고 따뜻하다", "날씨"),
    ("주말에 비가 온다고 한다", "날씨"),
]


def cosine_similarity(a: list[float], b: list[float]) -> float:
    """두 벡터의 방향이 얼마나 같은지 (-1 ~ 1). 1에 가까울수록 의미가 비슷하다."""
    dot = sum(x * y for x, y in zip(a, b))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(y * y for y in b))
    return dot / (norm_a * norm_b)


def run(model: str) -> None:
    texts = [text for text, _ in sentences]

    ollama.embed(model=model, input=texts[:1]) 
    start = time.perf_counter()
    vectors = ollama.embed(model=model, input=texts)["embeddings"]
    elapsed = time.perf_counter() - start

    print(f"=== {model} ===")
    print(f"벡터 길이(차원): {len(vectors[0])} | 문장 {len(texts)}개 임베딩: {elapsed:.3f}초")

    same, diff, pairs = [], [], []
    for i in range(len(sentences)):
        for j in range(i + 1, len(sentences)):
            score = cosine_similarity(vectors[i], vectors[j])
            is_same = sentences[i][1] == sentences[j][1]
            (same if is_same else diff).append(score)
            pairs.append((score, is_same, texts[i], texts[j]))

    for score, is_same, a, b in sorted(pairs, reverse=True):
        mark = "같은주제" if is_same else "다른주제"
        print(f"  {score:.3f} [{mark}] {a}  <->  {b}")

    avg_same = sum(same) / len(same)
    avg_diff = sum(diff) / len(diff)
    print(f"  같은 주제 평균 {avg_same:.3f} - 다른 주제 평균 {avg_diff:.3f} = 차이 {avg_same - avg_diff:+.3f}")
    print("  → 차이가 클수록(양수) 의미를 잘 구분하는 모델\n")


if __name__ == "__main__":
    for model in MODELS:
        try:
            run(model)
        except ollama.ResponseError as error:
            print(f"=== {model} === 실행 실패: {error.error} (ollama pull {model} 했는지 확인)\n")
