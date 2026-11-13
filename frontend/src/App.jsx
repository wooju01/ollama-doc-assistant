import { useState } from "react";
import QuestionAnswer from "./componets/QuestionAnswer";
import SummaryRequest from "./componets/SummaryRequest";

const TABS = [
  { id: "question", label: "문서에 질문하기" },
  { id: "summary", label: "문서 요약" },
];

export default function App() {
  const [tab, setTab] = useState("question");
  const [text, setText] = useState("");
  const [fileName, setFileName] = useState("");

  async function handleFileChange(event) {
    const file = event.target.files?.[0];
    if (!file) return;

    setText(await file.text());
    setFileName(file.name);
    event.target.value = "";
  }

  return (
    <main className="mx-auto max-w-3xl px-4 py-10">
      <h1 className="mb-6 text-3xl font-bold">Ollama Doc Assistant</h1>

      <div role="tablist" className="mb-6 flex gap-1 border-b border-gray-200">
        {TABS.map(({ id, label }) => (
          <button
            key={id}
            role="tab"
            aria-selected={tab === id}
            onClick={() => setTab(id)}
            className={`-mb-px border-b-2 px-4 py-2 text-sm font-medium ${
              tab === id
                ? "border-blue-600 text-blue-600"
                : "border-transparent text-gray-500 hover:text-gray-700"
            }`}
          >
            {label}
          </button>
        ))}
      </div>

      {/* 탭을 바꿔도 입력·결과가 사라지지 않도록 숨기기만 한다 */}
      <div hidden={tab !== "question"}>
        <QuestionAnswer />
      </div>

      <div hidden={tab !== "summary"}>
        <div className="mb-2 flex items-center justify-between">
          <span className="block text-sm font-medium text-gray-700">
            요약할 문서
          </span>

          <label className="cursor-pointer rounded-lg border border-gray-300 px-3 py-1.5 text-sm hover:bg-gray-50">
            파일 첨부 (.md, .txt)
            <input
              type="file"
              accept=".md,.txt"
              onChange={handleFileChange}
              className="hidden"
            />
          </label>
        </div>

        {fileName && (
          <p className="mb-2 text-sm text-gray-500">첨부된 파일: {fileName}</p>
        )}
        <SummaryRequest text={text} />
      </div>
    </main>
  );
}
