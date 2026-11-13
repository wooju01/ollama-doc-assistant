import { useState } from "react";
import SummaryRequest from "./components/SummaryRequest";

export default function App() {
  const [text, setText] = useState("");

  return (
    <main className="mx-auto max-w-3xl px-4 py-10">
      <h1 className="mb-6 text-3xl font-bold">Ollama Doc Assistant</h1>

      <label
        htmlFor="doc-text"
        className="mb-2 block text-sm font-medium text-gray-700"
      >
        요약할 문서
      </label>
      <textarea
        id="doc-text"
        value={text}
        onChange={(event) => setText(event.target.value)}
        rows={10}
        placeholder="요약할 내용을 붙여넣으세요"
        className="w-full rounded-lg border border-gray-300 p-3 focus:border-blue-500 focus:outline-none focus:ring-2 focus:ring-blue-200"
      />

      <SummaryRequest text={text} />
    </main>
  );
}
