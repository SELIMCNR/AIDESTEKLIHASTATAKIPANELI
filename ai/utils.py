import pandas as pd

def preprocess_input(input_dict):
    # Str → float dönüşüm ve feature engineering
    age = float(input_dict["Yaş"])
    pulse = float(input_dict["Nabız"])
    systolic = float(input_dict["Sistolik"])
    diastolic = float(input_dict["Diyastolik"])
    temp = float(input_dict["Ateş"])

    return pd.DataFrame([{
        "Yaş": age,
        "Nabız": pulse,
        "Sistolik": systolic,
        "Diyastolik": diastolic,
        "Kan Basıncı Farkı": systolic - diastolic,
        "Kan Basıncı Oranı": systolic / diastolic,
        "Ateş Değişim Hızı": 0.0  # Default başlangıç değeri
    }])