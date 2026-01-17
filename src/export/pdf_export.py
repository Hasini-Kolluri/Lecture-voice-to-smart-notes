from fpdf import FPDF
import re

def _sanitize_text(text: str) -> str:
    """
    Remove emojis and unsupported unicode characters.
    """
    # Remove emojis & symbols
    text = re.sub(r'[^\x00-\x7F]+', '', text)
    return text


def export_pdf(notes: str, output_path="lecture_notes.pdf"):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Use core font (safe)
    pdf.set_font("Arial", size=11)

    usable_width = pdf.w - pdf.l_margin - pdf.r_margin

    notes = _sanitize_text(notes)

    for line in notes.split("\n"):
        line = line.strip()
        if not line:
            pdf.ln(4)
            continue

        pdf.multi_cell(
            w=usable_width,
            h=7,
            txt=line
        )

    pdf.output(output_path)
    return output_path
