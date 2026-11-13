import { useRef, useState } from "react";
import { uploadDocument } from "./api/documentApi";
import QuestionAnswer from "./componets/QuestionAnswer";
import SummaryRequest from "./componets/SummaryRequest";

const TABS = [
  { id: "question", label: "문서에 질문하기" },
  { id: "summary", label: "첨부 문서 (요약·질문)" },
];

export default function App() {
  const [tab, setTab] = useState("question");
  const [text, setText] = useState("");
  const [fileName, setFileName] = useState("");

  // 첨부 파일 색인 상태: idle | uploading | ready | error
  const [uploadStatus, setUploadStatus] = useState("idle");
  const [uploadedDoc, setUploadedDoc] = useState(null); // { source, chunks }
  const [uploadError, setUploadError] = useState("");
  const uploadIdRef = useRef(0);

  async function handleFileChange(event) {
    const file = event.target.files?.[0];
    event.target.value = "";
    if (!file) return;

    setText(await file.text());
    setFileName(file.name);

    // 파일을 연달아 바꾸면 늦게 끝난 예전 업로드 결과는 무시한다
    const uploadId = ++uploadIdRef.current;
    setUploadStatus("uploading");
    setUploadedDoc(null);
    setUploadError("");

    try {
      const data = await uploadDocument({ file });
      if (uploadId !== uploadIdRef.current) return;
      setUploadedDoc(data);
      setUploadStatus("ready");
    } catch (error) {
      if (uploadId !== uploadIdRef.current) return;
      setUploadError(error.message);
      setUploadStatus("error");
    }
  }

  return (
    <main className="mx-auto max-w-3xl px-4 py-10">
      <h1 className="mb-6 text-3xl font-bold">올리마 간단 프로젝트?</h1>

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
      <div hidden={tab !== "question"}>
        <QuestionAnswer />
      </div>

      <div hidden={tab !== "summary"} className="space-y-6">
        <div>
          <div className="mb-2 flex items-center justify-between">
            <span className="block text-sm font-medium text-gray-700">
              첨부할 문서
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
            <p className="mb-2 text-sm text-gray-500">
              첨부된 파일: {fileName}
            </p>
          )}
          <SummaryRequest text={text} />
        </div>

        {uploadStatus !== "idle" && (
          <div className="border-t border-gray-200 pt-6">
            <h2 className="mb-3 text-lg font-semibold">이 문서에 질문하기</h2>

            {uploadStatus === "uploading" && (
              <p className="text-sm text-gray-500">
                질문할 수 있도록 문서를 준비하고 있습니다... (조각내기 → 임베딩)
              </p>
            )}

            {uploadStatus === "error" && (
              <p className="rounded-lg border border-red-200 bg-red-50 p-3 text-sm text-red-700">
                {uploadError}
              </p>
            )}

            {uploadStatus === "ready" && uploadedDoc && (
              <>
                <p className="mb-3 text-sm text-gray-500">
                  {uploadedDoc.source} · 조각 {uploadedDoc.chunks}개 준비 완료 —
                  이 문서에서만 찾아서 답합니다.
                </p>
                <QuestionAnswer
                  key={uploadedDoc.source}
                  source={uploadedDoc.source}
                  placeholder={`${uploadedDoc.source}에 대해 질문하세요`}
                />
              </>
            )}
          </div>
        )}
      </div>
    </main>
  );
}
