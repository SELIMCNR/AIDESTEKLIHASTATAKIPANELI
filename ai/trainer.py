import pandas as pd
from xgboost import XGBClassifier
import joblib
import os




def train_model(data_path=r"C:\Users\btk02\OneDrive\Desktop\Yeni klasör\data\dataset.csv",
                save_path="data/model.pkl"):
    try:
        # Veri setini oku
        print("📥 Veri okunuyor...")
        df = pd.read_csv(data_path)

        if df.empty:
            raise ValueError("❗️dataset.csv dosyası boş. Eğitim yapılamaz.")

        print(f"✅ {len(df)} satır veri yüklendi.")

        # Feature engineering
        df["Kan Basıncı Farkı"] = df["Sistolik"] - df["Diyastolik"]
        df["Kan Basıncı Oranı"] = df["Sistolik"] / df["Diyastolik"]
        df["Ateş Değişim Hızı"] = (df["Ateş"] - df["Ateş"].shift(1)).fillna(0)

        X = df[["Yaş", "Nabız", "Sistolik", "Diyastolik",
                "Kan Basıncı Farkı", "Kan Basıncı Oranı", "Ateş Değişim Hızı"]]
        y = df["Hasta_mı"]

        # Model eğit
        print("🤖 Model eğitiliyor...")
        model = XGBClassifier(n_estimators=200, max_depth=10, learning_rate=0.1)
        model.fit(X, y)

        # Kayıt klasörü oluşturulmazsa hata almasın
        os.makedirs(os.path.dirname(save_path), exist_ok=True)

        # Modeli kaydet
        joblib.dump(model, save_path)
        print(f"✅ Model başarıyla kaydedildi: {os.path.abspath(save_path)}")

    except FileNotFoundError:
        print(f"❌ dataset.csv bulunamadı: {data_path}")

    except pd.errors.EmptyDataError:
        print("❌ dataset.csv dosyası boş veya hatalı.")

    except Exception as e:
        print(f"🚨 Eğitim sırasında beklenmeyen bir hata oluştu: {str(e)}")

if __name__ == "__main__":
    train_model()        