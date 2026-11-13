const API_BASE_URL = "http://localhost:8000";

export async function createSummary({ text, signal }) {
  const response = await fetch(`${API_BASE_URL}/api/v1/summaries`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ text }),
    signal,
  });

  if (!response.ok) {
    throw new Error(`요약 요청에 실패했습니다. (${response.status})`);
  }

  return response.json();
}
