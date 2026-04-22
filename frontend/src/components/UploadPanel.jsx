import { useState } from "react";

export default function UploadPanel({ setData }) {

  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleUpload = async () => {

    if (!file) {
      setError("Please upload a resume");
      return;
    }

    const formData = new FormData();
    formData.append("resume", file);

    setLoading(true);
    setError("");

    try {
      const response = await fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        body: formData
      });

      if (!response.ok) {
        throw new Error("Server error");
      }

      const data = await response.json();
      setData(data);

    } catch (err) {
      console.error(err);
      setError("Something went wrong. Try again.");
    }

    setLoading(false);
  };

  return (
    <div className="upload-panel">

      <h2>Upload Resume</h2>

      <div
        className="drop-zone"
        onDragOver={(e) => e.preventDefault()}
        onDrop={(e) => {
          e.preventDefault();
          const droppedFile = e.dataTransfer.files[0];
          setFile(droppedFile);
          setError("");
        }}
      >

        <input
          type="file"
          accept=".pdf,.txt,.doc,.docx,.jpg,.jpeg,.png"
          onChange={(e) => {
            setFile(e.target.files[0]);
            setError("");
          }}
        />

        <p>Drag & Drop or Select File</p>

        {file && (
          <p className="file-name">Selected: {file.name}</p>
        )}

        {error && (
          <p className="error">{error}</p>
        )}

        <button
          onClick={handleUpload}
          disabled={loading || !file}
        >
          {loading ? "Analyzing..." : "Analyze Resume"}
        </button>

        {loading && <div className="loader"></div>}

      </div>

    </div>
  );
}