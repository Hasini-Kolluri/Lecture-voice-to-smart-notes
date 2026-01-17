# 🎓 Lecture Voice to Smart Notes Generator

A Streamlit-based application that converts lecture audio or video files into clean, structured study notes using speech recognition, NLP, and the Gemini API.

--------------------------------------------------

✨ FEATURES

- Upload lecture audio or video files (wav, mp3, m4a, mp4)
- Automatic speech-to-text transcription using Whisper
- Text cleaning and chunking
- Keyword extraction using TF-IDF
- AI-generated notes using Gemini
- Multiple note styles:
  - Concise
  - Detailed
  - Exam-focused
- Export notes as TXT, PDF, or DOCX
- Simple and clean Streamlit UI

--------------------------------------------------

🧠 TECH STACK

- Python
- Streamlit
- OpenAI Whisper
- Gemini API
- Scikit-learn
- NLTK
- FPDF
- python-docx

--------------------------------------------------

📂 PROJECT STRUCTURE

lecture-voice-to-smart-notes/
│
├── app.py
├── main.py
├── requirements.txt
├── .env.example
│
├── src/
│   ├── asr/
│   │   └── whisper_transcribe.py
│   ├── nlp/
│   │   ├── text_cleaning.py
│   │   ├── chunking.py
│   │   ├── keyword_extraction.py
│   │   └── summarization.py
│   ├── notes/
│   │   └── note_formatter.py
│   ├── export/
│   │   ├── pdf_export.py
│   │   └── docx_export.py
│   └── pipeline.py

--------------------------------------------------

🔑 GEMINI API KEY SETUP

This project requires a Gemini API key.

Step 1:
Go to https://ai.google.dev  
Create a project and generate an API key.

Step 2:
Create a file named .env in the project root and add:

GEMINI_API_KEY=your_api_key_here

⚠️ Do NOT commit this file to GitHub.

--------------------------------------------------

📄 ENV EXAMPLE

The repository includes a file named .env.example with this content:

GEMINI_API_KEY=

This clearly shows where the API key should be added.

--------------------------------------------------

▶️ RUN THE PROJECT LOCALLY

1. Clone the repository:
git clone https://github.com/Hasini-Kolluri/Lecture-voice-to-smart-notes
cd Lecture-voice-to-smart-notes

2. Create and activate environment:
conda create -n lecture-notes python=3.10
conda activate lecture-notes

3. Install dependencies:
pip install -r requirements.txt

4. Run the app:
streamlit run app.py

--------------------------------------------------

📝 NOTE STYLES

Concise:
Short bullet points for quick revision.

Detailed:
Structured explanations with more depth.

Exam-focused:
Definitions, keywords, and important exam points.

--------------------------------------------------

⚠️ GEMINI FREE TIER NOTICE

Gemini free tier has request limits.

If you see:
AI service temporarily busy or overloaded

Wait 30–60 seconds and click Rerun.
You do NOT need to upload the file again.

--------------------------------------------------