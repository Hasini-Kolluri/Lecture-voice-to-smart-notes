# 🎙️ Lecture Voice to Notes

An end-to-end AI-powered application that converts lecture audio/video into structured, readable notes.
The system uses Automatic Speech Recognition (ASR), text chunking, and keyword extraction, wrapped inside an interactive Streamlit web interface.

This project helps students and educators automate note-taking and focus more on learning instead of writing.

--------------------------------------------------

🚀 FEATURES

- Upload lecture audio or video files
- Accurate speech-to-text transcription using OpenAI Whisper
- Intelligent text chunking for long lectures
- Keyword extraction using TF-IDF
- Export notes as DOCX and TXT
- Interactive Streamlit UI
- Modular and scalable codebase

--------------------------------------------------

🏗️ PROJECT STRUCTURE

lecture-voice-to-notes/
│
├── app.py                     → Streamlit UI
├── requirements.txt
│
├── src/
│   ├── asr/
│   │   └── whisper_transcribe.py
│   │
│   ├── processing/
│   │   ├── chunking.py
│   │   └── keyword_extraction.py
│   │
│   ├── export/
│   │   ├── docx_export.py
│   │   └── txt_export.py
│   │
│   └── pipeline.py            → End-to-end pipeline
│
└── README.md

--------------------------------------------------

🛠️ TECH STACK

- Python 3.10+
- OpenAI Whisper for speech-to-text
- Scikit-learn for TF-IDF keyword extraction
- NumPy and Pandas for text processing
- Streamlit for web UI
- python-docx for DOCX export
- FFmpeg for audio preprocessing

--------------------------------------------------

📦 INSTALLATION & SETUP

1. Clone the repository

git clone https://github.com/your-username/lecture-voice-to-notes.git
cd lecture-voice-to-notes

2. Create and activate virtual environment

conda create -n lecture-notes python=3.10 -y
conda activate lecture-notes

3. Install dependencies

pip install -r requirements.txt

Note: Make sure FFmpeg is installed and added to your system PATH.

--------------------------------------------------

▶️ RUNNING THE APPLICATION

streamlit run app.py

Then open your browser at:
http://localhost:8501

--------------------------------------------------

🔄 WORKFLOW

1. Upload lecture audio or video
2. Convert speech to text using Whisper
3. Clean and chunk long text
4. Extract important keywords using TF-IDF
5. Generate structured notes
6. Export notes as DOCX or TXT

--------------------------------------------------

📌 USE CASES

- College lecture note generation
- Online course transcription
- Exam revision notes
- Educational YouTube video notes

--------------------------------------------------

🧪 CURRENT LIMITATIONS

- No abstractive summarization yet
- Best performance with clear audio
- Uses CPU-based Whisper model by default

--------------------------------------------------

🔮 FUTURE ENHANCEMENTS

- LLM-based abstractive summarization
- Multilingual transcription
- Topic-wise note structuring
- Cloud deployment
- Keyword and topic visualization

------------------------------------------------

"Turn lectures into knowledge, automatically."
