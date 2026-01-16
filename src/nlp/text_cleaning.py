import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download required resources (only runs first time)
nltk.download("stopwords")
nltk.download("wordnet")

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words("english"))

# Common filler words in lectures
FILLER_WORDS = [
    "uh", "um", "you know", "like", "so", "basically",
    "actually", "okay", "right", "hmm"
]

def remove_fillers(text: str) -> str:
    """Remove common filler words from text"""
    for filler in FILLER_WORDS:
        text = re.sub(rf"\b{filler}\b", "", text, flags=re.IGNORECASE)
    return text


def clean_text(text: str) -> str:
    """
    Cleans raw Whisper transcript text
    """
    # Lowercase
    text = text.lower()

    # Remove filler words
    text = remove_fillers(text)

    # Remove special characters (keep alphabets and spaces)
    text = re.sub(r"[^a-zA-Z\s]", " ", text)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()

    # Tokenize
    tokens = text.split()

    # Remove stopwords and lemmatize
    cleaned_tokens = [
        lemmatizer.lemmatize(word)
        for word in tokens
        if word not in stop_words
    ]

    return " ".join(cleaned_tokens)
