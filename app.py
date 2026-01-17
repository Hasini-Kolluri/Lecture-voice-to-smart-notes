import streamlit as st
import tempfile
from src.pipeline import run_pipeline
from src.export.pdf_export import export_pdf
from src.export.docx_export import export_docx

st.set_page_config(
    page_title="Lecture Voice → Smart Notes",
    page_icon="🎧",
    layout="wide"
)

st.title("🎓 Lecture Voice → Smart Notes Generator")
st.markdown("Upload a lecture **audio/video** file and generate smart notes.")

uploaded_file = st.file_uploader(
    "🎙 Upload lecture file",
    type=["wav", "mp3", "m4a", "mp4", "mpeg"]
)

st.subheader("🧠 Choose Notes Style")

style = st.radio(
    "Notes type",
    ["Concise", "Detailed", "Exam-Focused"],
    horizontal=True
)

mode_map = {
    "Concise": "concise",
    "Detailed": "detailed",
    "Exam-Focused": "exam"
}

if st.button("🚀 Generate Notes"):
    if uploaded_file is None:
        st.warning("Please upload a file first.")
        st.stop()

    with st.spinner("⏳ Processing lecture..."):
        result = run_pipeline(
            uploaded_file=uploaded_file,
            mode=mode_map[style]
        )

    st.success("✅ Notes generated!")

    with st.expander("📜 Transcription"):
        st.write(result["transcript"])

    st.subheader("🔑 Keywords")
    st.write(", ".join(result["keywords"]))

    st.subheader("📝 Notes")
    st.write(result["notes"])

    # Downloads
    st.download_button(
        "⬇ Download TXT",
        data=result["notes"],
        file_name="lecture_notes.txt"
    )

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_pdf:
        export_pdf(result["notes"], tmp_pdf.name)
        st.download_button(
            "⬇ Download PDF",
            data=open(tmp_pdf.name, "rb"),
            file_name="lecture_notes.pdf"
        )

    with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as tmp_docx:
        export_docx(result["notes"], tmp_docx.name)
        st.download_button(
            "⬇ Download DOCX",
            data=open(tmp_docx.name, "rb"),
            file_name="lecture_notes.docx"
        )
