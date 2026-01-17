from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

PROMPTS = {
    "concise": """
Convert the lecture into SHORT, crisp study notes.
- Headings
- Bullet points
- Very brief
""",

    "detailed": """
Convert the lecture into DETAILED structured notes.
- Clear headings
- Bullet points
- Explanations where needed
""",

    "exam": """
Convert the lecture into EXAM-FOCUSED notes.
- Definitions
- Important points
- Possible questions
- Formulae (if any)
"""
}

def summarize_text(chunks, mode="concise"):
    text = " ".join(chunks)

    prompt = f"""
{PROMPTS.get(mode, PROMPTS['concise'])}

Lecture:
{text}
"""

    response = client.models.generate_content(
        model="models/gemini-flash-latest",
        contents=prompt
    )

    return response.text
