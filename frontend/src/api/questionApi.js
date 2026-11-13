const API_BASE_URL = "http://localhost:8000";

// source를 넘기면 그 문서에서만 찾는다
export async function createAnswer({ question, source, signal }) {
  const response = await fetch(`${API_BASE_URL}/api/v1/questions`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ question, source }),
    signal,
  });

  if (!response.ok) {
    throw new Error(`질문 요청에 실패했습니다. (${response.status})`);
  }

  return response.json();
}
