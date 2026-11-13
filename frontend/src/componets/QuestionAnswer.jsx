import { useRef, useState } from "react";
import ReactMarkdown from "react-markdown";
import { createAnswer } from "../api/questionApi";

export default function QuestionAnswer() {
  const [question, setQuestion] = useState("");
  const [askedQuestion, setAskedQuestion] = useState("");
  const [status, setStatus] = useState("idle");
  const [result, setResult] = useState(null);
  const [error, setError] = useState("");
  const controllerRef = useRef(null);

  async function ask(event) {
    event?.preventDefault();
    const trimmed = question.trim();
    if (!trimmed || status === "loading") return;

    const controller = new AbortController();
    controllerRef.current = controller;
    setAskedQuestion(trimmed);
    setStatus("loading");
    setError("");
    setResult(null);

    try {
      const data = await createAnswer({
        question: trimmed,
        signal: controller.signal,
      });
      setResult(data);
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
    <section aria-busy={status === "loading"} className="space-y-4">
      <form onSubmit={ask} className="flex gap-2">
        <label htmlFor="question" className="sr-only">
          질문
        </label>
        <input
          id="question"
          value={question}
          onChange={(event) => setQuestion(event.target.value)}
          maxLength={500}
          placeholder="문서에 대해 질문하세요 (예: npm이 뭐야?)"
          className="flex-1 rounded-lg border border-gray-300 px-3 py-2 focus:border-blue-500 focus:outline-none focus:ring-2 focus:ring-blue-200"
        />
        {status === "loading" ? (
          <button
            type="button"
            onClick={() => controllerRef.current?.abort()}
            className="rounded-lg border border-gray-300 px-4 py-2 hover:bg-gray-50"
          >
            취소
          </button>
        ) : (
          <button
            type="submit"
            disabled={!question.trim()}
            className="rounded-lg bg-blue-600 px-4 py-2 font-medium text-white hover:bg-blue-700 disabled:cursor-not-allowed disabled:bg-gray-300"
          >
            질문
          </button>
        )}
      </form>

      {status === "loading" && (
        <p className="text-gray-500">문서에서 찾아보고 있습니다...</p>
      )}
      {status === "cancelled" && (
        <p className="text-gray-500">요청을 취소했습니다.</p>
      )}

      {status === "error" && (
        <div className="rounded-lg border border-red-200 bg-red-50 p-4">
          <p className="text-red-700">{error}</p>
          <button
            onClick={ask}
            className="mt-2 text-sm font-medium text-red-700 underline"
          >
            다시 시도
          </button>
        </div>
      )}

      {status === "success" && result && (
        <div className="space-y-3">
          <p className="text-sm text-gray-500">Q. {askedQuestion}</p>

          <div className="prose max-w-none rounded-lg border border-gray-200 bg-gray-50 p-5">
            <ReactMarkdown>{result.answer}</ReactMarkdown>
          </div>

          {result.sources.length > 0 ? (
            <div>
              <h2 className="mb-2 text-sm font-medium text-gray-700">
                출처 ({result.sources.length})
              </h2>
              <ul className="space-y-2">
                {result.sources.map((source) => (
                  <li
                    key={`${source.source}-${source.heading}`}
                    className="rounded-lg border border-gray-200"
                  >
                    <details>
                      <summary className="cursor-pointer px-3 py-2 text-sm">
                        <span className="font-medium">{source.source}</span>
                        <span className="text-gray-500">
                          {" "}
                          › {source.heading}
                        </span>
                        <span className="ml-2 text-xs text-gray-400">
                          유사도 {source.score.toFixed(3)}
                        </span>
                      </summary>
                      <pre className="overflow-x-auto whitespace-pre-wrap border-t border-gray-200 bg-white p-3 text-xs text-gray-700">
                        {source.text}
                      </pre>
                    </details>
                  </li>
                ))}
              </ul>
            </div>
          ) : (
            <p className="text-sm text-gray-500">
              문서에 관련 내용이 없거나, 질문이 너무 넓을 수 있어요. 구체적으로
              다시 물어보세요. (예: &quot;개발 서버는 어떻게 꺼?&quot;)
            </p>
          )}
        </div>
      )}
    </section>
  );
}
