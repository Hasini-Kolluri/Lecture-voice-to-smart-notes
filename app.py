import streamlit as st
import tempfile
import os

from src.pipeline import run_pipeline
from src.export.docx_export import export_docx
from src.export.pdf_export import export_pdf

# --------------------------------------------------
# Page config
# --------------------------------------------------
st.set_page_config(
    page_title="Lecture Voice → Smart Notes",
    page_icon="🎓",
    layout="wide"
)

# --------------------------------------------------
# Header
# --------------------------------------------------
st.title("🎓 Lecture Voice → Smart Notes Generator")
st.caption(
    "Upload a lecture audio/video file to generate transcripts, "
    "key concepts, and AI-powered study notes."
)

st.info("⏱ Long lectures may take 1–3 minutes. Upload once and wait for processing.")

st.divider()

# --------------------------------------------------
# File uploader
# --------------------------------------------------
uploaded_audio = st.file_uploader(
    "🎙 Upload lecture file",
    type=["wav", "mp3", "m4a", "mp4", "mpeg", "mpg"],
    help="Supported formats: WAV, MP3, M4A, MP4, MPEG"
)

# --------------------------------------------------
# Run pipeline (FILE-AWARE CACHE)
# --------------------------------------------------
if uploaded_audio is not None:

    # Create a unique ID for the uploaded file
    file_id = f"{uploaded_audio.name}_{uploaded_audio.size}"

    # Run Gemini ONLY if a new file is uploaded
    if (
        "last_file_id" not in st.session_state
        or st.session_state.last_file_id != file_id
    ):
        with st.spinner("⏳ Processing lecture… please wait"):
            st.session_state.result = run_pipeline(uploaded_audio)
            st.session_state.last_file_id = file_id

    result = st.session_state.result

    # --------------------------------------------------
    # Error handling
    # --------------------------------------------------
    if "error" in result:
        st.error(
            "⚠️ The AI service is temporarily busy or overloaded.\n\n"
            "Please wait 30–60 seconds and click **Rerun**.\n"
            "Your file does NOT need to be uploaded again."
        )
        st.stop()


    st.success("✅ Notes generated successfully")
    st.divider()

    # --------------------------------------------------
    # Tabs
    # --------------------------------------------------
    tab_notes, tab_keywords, tab_transcript = st.tabs(
        ["📝 Notes", "🔑 Keywords", "📜 Transcription"]
    )

    # --------------------------------------------------
    # NOTES TAB
    # --------------------------------------------------
    with tab_notes:
        st.subheader("AI-Generated Notes")

        notes_text = result["notes"]

        # Preview + expand
        preview_len = 1200
        if len(notes_text) > preview_len:
            st.markdown(notes_text[:preview_len] + "…")
            with st.expander("Show full notes"):
                st.markdown(notes_text)
        else:
            st.markdown(notes_text)

        # Copy-friendly view
        with st.expander("📋 Copy notes"):
            st.code(notes_text, language="markdown")

    # --------------------------------------------------
    # KEYWORDS TAB
    # --------------------------------------------------
    with tab_keywords:
        st.subheader("Key Concepts")

        if result["keywords"]:
            chips = " ".join(
                [
                    f"<span style='background:#2e7d32;"
                    f"padding:6px 12px;border-radius:14px;"
                    f"color:white;font-size:14px'>"
                    f"{kw}</span>"
                    for kw in result["keywords"]
                ]
            )
            st.markdown(chips, unsafe_allow_html=True)
        else:
            st.info("No keywords detected.")

    # --------------------------------------------------
    # TRANSCRIPTION TAB
    # --------------------------------------------------
    with tab_transcript:
        st.subheader("Full Transcription")
        st.write(result["transcript"])

    st.divider()

    # --------------------------------------------------
    # Downloads
    # --------------------------------------------------
    with st.expander("⬇ Download options"):
        # TXT
        st.download_button(
            label="📄 Download as TXT",
            data=result["notes"],
            file_name="lecture_notes.txt",
            mime="text/plain"
        )

        # DOCX
        with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as tmp_docx:
            docx_path = export_docx(result["notes"], tmp_docx.name)

        with open(docx_path, "rb") as f:
            st.download_button(
                label="📘 Download as DOCX",
                data=f,
                file_name="lecture_notes.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )

        # PDF
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_pdf:
            pdf_path = export_pdf(result["notes"], tmp_pdf.name)

        with open(pdf_path, "rb") as f:
            st.download_button(
                label="📕 Download as PDF",
                data=f,
                file_name="lecture_notes.pdf",
                mime="application/pdf"
            )

# --------------------------------------------------
# Footer
# --------------------------------------------------
st.caption(
    "⚙️ Audio is processed locally. Notes are generated using Whisper and Gemini."
)
