import joblib
import numpy as np
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

# 1. Inisialisasi FastAPI
app = FastAPI(
    title="Heart Disease Prediction API",
    description="API untuk memprediksi risiko penyakit jantung menggunakan model ML",
    version="1.0"
)

# 2. Muat Model Terbaik Hasil Tuning (.pkl)
# Pastikan file 'best_model_heart_disease.pkl' sudah ada di folder yang sama atau sesuai jalurnya
try:
    model = joblib.load("Membangun_model/best_model_heart_disease.pkl")
    print("Model berhasil dimuat!")
except:
    model = joblib.load("best_model_heart_disease.pkl")
    print("Model berhasil dimuat dari direktori lokal!")

# 3. Definisikan Struktur Data Input (Sesuaikan dengan fitur dataset kamu)
# Ini adalah contoh fitur umum pada dataset heart disease (misal: age, sex, cp, trestbps, dll.)
class PatientData(BaseModel):
    features: list  # Menerima input dalam bentuk list angka/fitur

# 4. Endpoint Utama untuk Prediksi
@app.post("/predict", tags=["Prediction"])
def predict(data: PatientData):
    # Mengubah data input menjadi array 2D untuk model
    input_data = np.array(data.features).reshape(1, -1)
    
    # Melakukan prediksi (0 = Sehat, 1 = Penyakit Jantung)
    prediction = model.predict(input_data)
    prediction_proba = model.predict_proba(input_data)
    
    # Menentukan hasil teks
    status = "Terindikasi Penyakit Jantung" if prediction[0] == 1 else "Jantung Sehat / Normal"
    
    return {
        "prediction": int(prediction[0]),
        "status": status,
        "confidence_score": float(np.max(prediction_proba))
    }

# 5. Endpoint Cek Status Server (Health Check)
@app.get("/", tags=["General"])
def index():
    return {"message": "API Prediksi Penyakit Jantung Aktif!"}

if __name__ == "__main__":
    # Ubah menjadi seperti ini
    uvicorn.run(app, host="127.0.0.1", port=8000)