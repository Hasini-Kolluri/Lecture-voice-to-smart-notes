from src.asr.whisper_transcribe import transcribe_audio
from src.nlp.text_cleaning import clean_text
from src.nlp.chunking import chunk_text
from src.nlp.keyword_extraction import extract_keywords
from src.nlp.summarization import summarize_text

def run_pipeline(uploaded_file, mode="concise"):
    # Save uploaded file temporarily
    import tempfile

    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(uploaded_file.read())
        audio_path = tmp.name

    # 1. Transcription
    transcript = transcribe_audio(audio_path)

    # 2. Cleaning
    cleaned_text = clean_text(transcript)

    # 3. Chunking
    chunks = chunk_text(cleaned_text)

    # 4. Keywords
    keywords = extract_keywords(cleaned_text)

    # 5. Summarization (MODE BASED)
    notes = summarize_text(chunks, mode=mode)

    return {
        "transcript": transcript,
        "keywords": keywords,
        "notes": notes
    }
