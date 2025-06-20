from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime
import os

def save_pdf(data_dict, result, path="raporlar"):
    os.makedirs(path, exist_ok=True)
    filename = f"{data_dict.get('Ad Soyad','Hasta')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    pdf_path = os.path.join(path, filename)

    c = canvas.Canvas(pdf_path, pagesize=A4)
    width, height = A4

    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, height - 50, "🩺 AI Hasta Tahmin Raporu")
    c.setFont("Helvetica", 12)

    y = height - 100
    for key, value in data_dict.items():
        c.drawString(50, y, f"{key}: {value}")
        y -= 20

    c.drawString(50, y - 10, f"Tahmin Sonucu: {'Hasta' if result == 1 else 'Sağlıklı'}")
    c.drawString(50, y - 40, f"Tarih: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    c.showPage()
    c.save()

    return pdf_path