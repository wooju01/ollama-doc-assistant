import { useRef, useState } from "react";
import ReactMarkdown from "react-markdown";
import { createSummary } from "../api/summaryApi";

export default function SummaryRequest({ text }) {
  const [status, setStatus] = useState("idle");
  const [summary, setSummary] = useState("");
  const [error, setError] = useState("");
  const controllerRef = useRef(null);

  async function requestSummary() {
    if (!text.trim() || status === "loading") return;

    const controller = new AbortController();
    controllerRef.current = controller;
    setStatus("loading");
    setError("");

    try {
      const data = await createSummary({ text, signal: controller.signal });
      setSummary(data.summary);
      setStatus("success");
    } catch (requestError) {
      if (requestError.name === "AbortError") {
        setStatus("cancelled");
      } else {
        setError(requestError.message);
        setStatus("error");
      }
    } finally {
      controllerRef.current = null;
    }
  }

  return (
    <section aria-busy={status === "loading"} className="mt-4 space-y-4">
      <div className="flex gap-2">
        <button
          onClick={requestSummary}
          disabled={!text.trim() || status === "loading"}
          className="rounded-lg bg-blue-600 px-4 py-2 font-medium text-white hover:bg-blue-700 disabled:cursor-not-allowed disabled:bg-gray-300"
        >
          {status === "loading" ? "요약 중..." : "요약 요청"}
        </button>

        {status === "loading" && (
          <button
            type="button"
            onClick={() => controllerRef.current?.abort()}
            className="rounded-lg border border-gray-300 px-4 py-2 hover:bg-gray-50"
          >
            취소
          </button>
        )}
      </div>

      {status === "loading" && (
        <p className="text-gray-500">요약을 생성하고 있습니다.</p>
      )}
      {status === "cancelled" && (
        <p className="text-gray-500">요청을 취소했습니다.</p>
      )}

      {status === "error" && (
        <div className="rounded-lg border border-red-200 bg-red-50 p-4">
          <p className="text-red-700">{error}</p>
          <button
            onClick={requestSummary}
            className="mt-2 text-sm font-medium text-red-700 underline"
          >
            다시 시도
          </button>
        </div>
      )}

      {status === "success" && (
        <div className="prose max-w-none rounded-lg border border-gray-200 bg-gray-50 p-5">
          <ReactMarkdown>{summary}</ReactMarkdown>
        </div>
      )}
    </section>
  );
}
