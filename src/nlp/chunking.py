import nltk
from nltk.tokenize import sent_tokenize

# Download required resource (runs only once)
nltk.download("punkt")


def chunk_text(
    text: str,
    max_words: int = 400
) -> list:
    """
    Splits cleaned text into semantically meaningful chunks
    without breaking sentences.
    """

    sentences = sent_tokenize(text)

    chunks = []
    current_chunk = []
    current_word_count = 0

    for sentence in sentences:
        word_count = len(sentence.split())

        # If adding sentence exceeds max size, finalize chunk
        if current_word_count + word_count > max_words:
            chunks.append(" ".join(current_chunk))
            current_chunk = [sentence]
            current_word_count = word_count
        else:
            current_chunk.append(sentence)
            current_word_count += word_count

    # Add remaining chunk
    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks


# Optional test
if __name__ == "__main__":
    sample_text = (
        "Machine learning is a subset of artificial intelligence. "
        "It focuses on building systems that learn from data. "
        "These systems improve automatically through experience."
    )
    result = chunk_text(sample_text, max_words=10)
    print(result)
