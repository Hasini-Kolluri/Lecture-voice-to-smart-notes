# 🎙️ Lecture Voice to Notes

An end-to-end AI-powered application that converts lecture audio/video into structured, readable notes.
The system uses Automatic Speech Recognition (ASR), text chunking, and keyword extraction, wrapped inside an interactive Gradio web interface.

This project helps students and educators automate note-taking and focus more on learning instead of writing.

--------------------------------------------------

🚀 FEATURES

- Upload lecture audio or video files
- Accurate speech-to-text transcription using OpenAI Whisper
- Intelligent text chunking for long lectures
- Generates structured, readable notes
- Keyword extraction using TF-IDF
- Export notes as DOCX and TXT
- Interactive Gradio UI
- Modular and scalable codebase

--------------------------------------------------
<pre>

🏗️ PROJECT STRUCTURE

lecture-voice-to-smart-notes/
│
├── gradio_app.py → Gradio web interface
├── requirements.txt
├── .env.example → Environment variable template
│
├── src/
│ ├── asr/
│ │ └── whisper_transcribe.py → Audio to text (Whisper)
│ │
│ ├── nlp/
│ │ ├── text_cleaning.py → Text preprocessing
│ │ ├── chunking.py → Long text chunking
│ │ ├── keyword_extraction.py → TF-IDF keywords
│ │ └── summarization.py → Notes generation logic
│ │
│ ├── notes/
│ │ └── note_formatter.py → Final note formatting
│ │
│ ├── export/
│ │ └── docx_export.py → DOCX export
│ │
│ └── pipeline.py → End-to-end processing pipeline
│
└── README.md

</pre>
--------------------------------------------------

🛠️ TECH STACK

- Python 3.10+
- OpenAI Whisper for speech-to-text
- Scikit-learn for TF-IDF keyword extraction
- NLTK for text processing
- Gradio for web UI
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

python gradio_app.py

Then open your browser at:
http://localhost:7860

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
