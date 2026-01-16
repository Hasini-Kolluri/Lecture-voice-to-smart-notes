import os
import tempfile
from typing import Union
from pydub import AudioSegment

from src.asr.whisper_transcribe import transcribe_audio
from src.nlp.text_cleaning import clean_text
from src.nlp.chunking import chunk_text
from src.nlp.keyword_extraction import extract_keywords
from src.nlp.summarization import summarize_text
from src.notes.note_formatter import format_notes


def run_pipeline(uploaded_audio: Union[str, object]) -> dict:
    temp_files = []

    try:
        # 1️⃣ Save file
        if hasattr(uploaded_audio, "read"):
            suffix = uploaded_audio.name.split(".")[-1].lower()
            with tempfile.NamedTemporaryFile(delete=False, suffix=f".{suffix}") as tmp:
                tmp.write(uploaded_audio.read())
                input_path = tmp.name
                temp_files.append(input_path)
        else:
            input_path = uploaded_audio
            suffix = input_path.split(".")[-1].lower()

        # 2️⃣ Convert MP4/MPEG → WAV
        if suffix in ["mp4", "mpeg", "mpg"]:
            audio = AudioSegment.from_file(input_path)
            with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as wav_tmp:
                wav_path = wav_tmp.name
            audio.export(wav_path, format="wav")
            audio_path = wav_path
            temp_files.append(wav_path)
        else:
            audio_path = input_path

        # 3️⃣ Transcription
        transcript = transcribe_audio(audio_path)

        # 4️⃣ Cleaning
        cleaned_text = clean_text(transcript)

        # 5️⃣ Chunking (used only for formatting)
        chunks = chunk_text(cleaned_text)

        # 6️⃣ Keywords (ONCE)
        keywords = extract_keywords(cleaned_text)

        # 7️⃣ Summarization (ONCE — IMPORTANT)
        summary = summarize_text(cleaned_text)
        summaries = [summary]

        # 8️⃣ Formatting
        notes = format_notes(summaries)

        return {
            "transcript": transcript,
            "cleaned_text": cleaned_text,
            "chunks": chunks,
            "keywords": keywords,
            "summary": summary,
            "notes": notes
        }

    except Exception as e:
        return {"error": str(e)}

    finally:
        for f in temp_files:
            if os.path.exists(f):
                os.remove(f)
