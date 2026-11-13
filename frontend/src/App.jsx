import { useState } from "react";
import SummaryRequest from "./componets/SummaryRequest";

export default function App() {
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

      <div className="mb-2 flex items-center justify-between">
        <label
          htmlFor="doc-text"
          className="block text-sm font-medium text-gray-700"
        >
          요약할 문서
        </label>

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
    </main>
  );
}
