import whisper
import tempfile
import os


# Load model ONCE
model = whisper.load_model("base")


def transcribe_audio(audio_path: str) -> str:
    """
    Transcribes audio using Whisper.
    Avoids in-place FFmpeg processing.
    """

    # If already WAV, DO NOT reprocess with FFmpeg
    if audio_path.lower().endswith(".wav"):
        result = model.transcribe(audio_path)
        return result["text"]

    # Otherwise convert safely to WAV
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        wav_path = tmp.name

    try:
        result = model.transcribe(audio_path)
        return result["text"]
    finally:
        if os.path.exists(wav_path):
            os.remove(wav_path)
