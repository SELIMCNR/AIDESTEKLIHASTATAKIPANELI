import csv
from datetime import datetime
from ai.model import load_model, predict
import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from app.pdf_writer import save_pdf  # Dosyanın yoluna göre düzelt


class Controller:
    def __init__(self):
        self.model = load_model()
   
    def predict_patient(self, input_data):
        result = predict(self.model, input_data)
        self.log_to_csv(input_data, result)
        save_pdf(input_data, result)  # PDF olarak kaydet
        # Bellekteki veriyi temizle
        for key in list(input_data.keys()):
            input_data[key] = ""
        
        return result

    def log_to_csv(self, input_data, result):
        log_path = "data/logs.csv"
        os.makedirs("data", exist_ok=True)

        with open(log_path, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            # Eğer dosya boşsa başlıkları yaz
            if file.tell() == 0:
                writer.writerow(["Ad", "Yaş", "Nabız", "Sistolik", "Diyastolik", "Ateş", "Tahmin", "Zaman"])

            writer.writerow([
                input_data.get("Ad Soyad", ""),
                input_data.get("Yaş", ""),
                input_data.get("Nabız", ""),
                input_data.get("Sistolik", ""),
                input_data.get("Diyastolik", ""),
                input_data.get("Ateş", ""),
                result,
                datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ])
            