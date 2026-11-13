const API_BASE_URL = "http://localhost:8000";

export async function createAnswer({ question, signal }) {
  const response = await fetch(`${API_BASE_URL}/api/v1/questions`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ question }),
    signal,
  });

  if (!response.ok) {
    throw new Error(`질문 요청에 실패했습니다. (${response.status})`);
  }

  return response.json();
}
