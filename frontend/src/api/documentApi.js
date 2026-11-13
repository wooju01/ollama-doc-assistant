const API_BASE_URL = "http://localhost:8000";

export async function uploadDocument({ file, signal }) {
  const formData = new FormData();
  formData.append("file", file);

  // FormData를 보낼 때는 Content-Type을 직접 넣지 않는다 (브라우저가 boundary까지 채워 준다)
  const response = await fetch(`${API_BASE_URL}/api/v1/documents`, {
    method: "POST",
    body: formData,
    signal,
  });

  if (!response.ok) {
    const body = await response.json().catch(() => null);
    throw new Error(
      typeof body?.detail === "string"
        ? body.detail
        : `문서 업로드에 실패했습니다. (${response.status})`,
    );
  }

  return response.json();
}
