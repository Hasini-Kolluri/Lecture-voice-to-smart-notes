import os
import time
import streamlit as st
from dotenv import load_dotenv
from google import genai
from google.genai.errors import ClientError

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def _call_gemini_with_retry(prompt: str, retries: int = 3):
    """
    Retry Gemini calls when the model is overloaded (503).
    """
    for i in range(retries):
        try:
            return client.models.generate_content(
                model="models/gemini-flash-latest",
                contents=prompt
            )
        except ClientError as e:
            # Retry only for temporary overload
            if "UNAVAILABLE" in str(e) or "503" in str(e):
                time.sleep(2 ** i)  # 1s, 2s, 4s
            else:
                raise
    raise RuntimeError("Gemini is temporarily overloaded. Please retry in a minute.")

@st.cache_data(show_spinner=False)
def summarize_text(text: str) -> str:
    prompt = f"""
Convert the following lecture transcript into clean, structured study notes.

Rules:
- Clear headings
- Bullet points
- Academic tone
- No emojis
- No dates or metadata

Transcript:
{text}
"""
    response = _call_gemini_with_retry(prompt)
    return response.text
