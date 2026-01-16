import os
import time
import streamlit as st
from typing import Union, List
from dotenv import load_dotenv
from google import genai
from google.genai.errors import ClientError

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def _call_gemini_with_retry(prompt: str, retries: int = 3):
    for i in range(retries):
        try:
            return client.models.generate_content(
                model="models/gemini-flash-latest",
                contents=prompt
            )
        except ClientError as e:
            if "UNAVAILABLE" in str(e) or "503" in str(e):
                time.sleep(2 ** i)
            else:
                raise
    raise RuntimeError("Gemini is temporarily overloaded. Please retry.")

@st.cache_data(show_spinner=False)
def extract_keywords(
    text: Union[str, List[str]],
    top_n: int = 10
) -> List[str]:

    if isinstance(text, list):
        text = " ".join(text)

    prompt = f"""
Extract {top_n} important academic keywords or key phrases.

Rules:
- Ignore words like lecture, audio, transcription
- Prefer subject-specific concepts
- 1–3 words per keyword
- Return ONLY a comma-separated list

Text:
{text}
"""

    response = _call_gemini_with_retry(prompt)
    return [k.strip() for k in response.text.split(",") if k.strip()]
