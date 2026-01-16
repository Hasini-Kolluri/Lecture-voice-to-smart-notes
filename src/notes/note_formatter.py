from datetime import datetime


def format_notes(
    summaries: list,
    title: str = "Lecture Notes"
) -> str:
    """
    Convert summarized chunks into structured lecture notes
    """

    formatted_notes = []

    # Header
    formatted_notes.append("📘 " + title)
    formatted_notes.append(f"🗓 Generated on: {datetime.now().strftime('%d %B %Y')}")
    formatted_notes.append("\n" + "=" * 50 + "\n")

    # Body
    for idx, summary in enumerate(summaries, 1):
        formatted_notes.append(f"🔹 Topic {idx}")
        formatted_notes.append(f"• {summary}\n")

    return "\n".join(formatted_notes)


# Optional test
if __name__ == "__main__":
    test_summaries = [
        "Machine learning is a subset of artificial intelligence focused on learning from data.",
        "Supervised learning uses labeled datasets to train predictive models."
    ]

    print(format_notes(test_summaries))
