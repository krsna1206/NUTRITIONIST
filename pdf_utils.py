from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO


def generate_nutrition_pdf(response_text):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4)
    styles = getSampleStyleSheet()
    elements = []

    lines = response_text.strip().split("\n")

    # Extract dish name
    dish_name = lines[0].replace("Dish Name:", "").strip()
    elements.append(Paragraph(f"<b>Dish Name:</b> {dish_name}", styles["Title"]))
    elements.append(Spacer(1, 12))

    # Extract table
    table_data = []
    for line in lines:
        if "|" in line:
            row = [cell.strip() for cell in line.split("|")]
            table_data.append(row)

    table = Table(table_data, repeatRows=1)
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
        ("GRID", (0, 0), (-1, -1), 1, colors.black),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("ALIGN", (1, 1), (-1, -1), "CENTER"),
    ]))

    elements.append(table)
    doc.build(elements)

    buffer.seek(0)
    return buffer
