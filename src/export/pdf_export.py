from fpdf import FPDF
import re

def export_pdf(notes: str, output_path="lecture_notes.pdf"):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    pdf.add_font("DejaVu", "", "DejaVuSans.ttf", uni=True)
    pdf.add_font("DejaVu-Bold", "", "DejaVuSans-Bold.ttf", uni=True)

    pdf.set_font("DejaVu", size=12)

    for raw_line in notes.split("\n"):
        line = raw_line.strip()

        if not line:
            pdf.ln(4)
            continue

        if re.match(r"^(#+|\*\*)", line):
            text = re.sub(r"^(#+|\*\*)", "", line).strip()
            pdf.set_font("DejaVu-Bold", size=15)
            pdf.multi_cell(0, 10, text)
            pdf.ln(2)
            pdf.set_font("DejaVu", size=12)
            continue

        if line.startswith(("-", "•")):
            pdf.multi_cell(0, 8, "• " + line.lstrip("-• "))
            continue

        pdf.multi_cell(0, 8, line)

    pdf.output(output_path)
    return output_path
