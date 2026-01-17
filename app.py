import io
import gradio as gr
import tempfile

from src.pipeline import run_pipeline
from src.export.docx_export import export_docx


def generate_notes(uploaded_file, style):
    if uploaded_file is None:
        return "❌ Please upload a lecture file.", "", "", None, None

    mode_map = {
        "Concise": "concise",
        "Detailed": "detailed",
        "Exam-Focused": "exam"
    }

    # ---- FIX: Convert Gradio file → Streamlit-like file ----
    with open(uploaded_file, "rb") as f:
        file_bytes = f.read()

    streamlit_like_file = io.BytesIO(file_bytes)
    streamlit_like_file.name = uploaded_file  # required by whisper

    # --------------------------------------------------------

    result = run_pipeline(
        uploaded_file=streamlit_like_file,
        mode=mode_map[style]
    )

    # Save TXT
    txt_file = tempfile.NamedTemporaryFile(delete=False, suffix=".txt")
    txt_file.write(result["notes"].encode("utf-8"))
    txt_file.close()

    # Save DOCX
    docx_file = tempfile.NamedTemporaryFile(delete=False, suffix=".docx")
    export_docx(result["notes"], docx_file.name)

    return (
        result["transcript"],
        ", ".join(result["keywords"]),
        result["notes"],
        txt_file.name,
        docx_file.name
    )


with gr.Blocks(title="Lecture Voice → Smart Notes") as demo:
    gr.Markdown("# 🎓 Lecture Voice → Smart Notes Generator")
    gr.Markdown(
        "Upload a **lecture audio/video file** and generate smart notes using ML + NLP."
    )

    with gr.Row():
        lecture_file = gr.File(
            label="🎙 Upload Lecture File",
            file_types=[".wav", ".mp3", ".m4a", ".mp4", ".mpeg"]
        )

        style = gr.Radio(
            ["Concise", "Detailed", "Exam-Focused"],
            label="🧠 Choose Notes Style",
            value="Concise"
        )

    generate_btn = gr.Button("🚀 Generate Notes")

    with gr.Tab("📜 Transcription"):
        transcript_out = gr.Textbox(lines=10, interactive=False)

    with gr.Tab("🔑 Keywords"):
        keywords_out = gr.Textbox(interactive=False)

    with gr.Tab("📝 Notes"):
        notes_out = gr.Textbox(lines=15, interactive=False)

    gr.Markdown("### ⬇ Download Files")

    with gr.Row():
        txt_download = gr.File(label="TXT")
        docx_download = gr.File(label="DOCX")

    generate_btn.click(
        fn=generate_notes,
        inputs=[lecture_file, style],
        outputs=[
            transcript_out,
            keywords_out,
            notes_out,
            txt_download,
            docx_download
        ]
    )


if __name__ == "__main__":
    demo.launch()
