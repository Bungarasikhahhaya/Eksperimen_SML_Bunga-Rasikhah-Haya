# Heart Disease Prediction Project (End-to-End MLOps Pipeline)

Proyek ini merupakan implementasi pipeline MLOps *end-to-end* untuk mendeteksi risiko penyakit jantung berdasarkan data kesehatan pasien. Proyek ini mencakup tahap pengembangan model (*modelling & tuning*), pelacakan eksperimen, otomatisasi workflow (CI/CD), penyajian model (*serving/inference*), hingga sistem monitoring dan *alerting* secara real-time.

---

🚀 Komponen Sistem & Cara Menjalankan
1. Tahap Membangun Model & Pelacakan Eksperimen
Proyek ini menggunakan Random Forest Classifier yang dioptimalkan menggunakan GridSearchCV pada skrip modelling_tuning.py.

Eksperimen Tracking: Menggunakan MLflow yang diintegrasikan langsung dengan DagsHub untuk melacak parameter terbaik, nilai akurasi, dan menyimpan artifak model secara cloud.

Cara Menjalankan Lokal:

Bash
cd MLProject_Folder
pip install -r requirements.txt
python modelling_tuning.py
2. MLflow Project Configuration
File MLProject dan conda.yaml disediakan agar pipeline pelatihan model ini bersifat reproducible (dapat dijalankan di lingkungan lain secara identik oleh MLflow CLI).

3. Model Serving (API Inference)
Model terbaik disajikan dalam bentuk REST API menggunakan FastAPI dan server Uvicorn pada skrip 7.Inference.py.

Cara Menjalankan Server:

Bash
python "Monitoring dan Logging/7.Inference.py"
Akses API Dokumentasi (Swagger UI): Buka browser dan akses http://localhost:8000/docs untuk melakukan uji coba prediksi lewat endpoint POST /predict.

4. Monitoring & Alerting (Prometheus + Grafana)
Metrics Exporter: Skrip 3.prometheus_exporter.py bertindak untuk mengekspos metrik kustom seperti model_accuracy_ratio ke server Prometheus.

Prometheus: Memantau ketersediaan target eksportir (UP) pada port yang ditentukan.

Grafana Dashboard: Menampilkan visualisasi data performa model secara real-time.

Alerting System: Mengonfigurasi aturan alarm di Grafana (e.g., Accuracy Drop, High CPU, HTTP Errors). Jika metrik menyentuh ambang batas (threshold), status akan berubah menjadi Firing dan mengirimkan notifikasi peringatan langsung ke Email.

🔗 Tautan Platform Pihak Ketiga
Informasi detail mengenai tautan eksternal proyek ini dapat diakses pada file teks di dalam folder utama:

DagsHub Repository (MLflow Tracking): Terlampir di MLProject_Folder/dagsHub.txt

Docker Hub Repository (Container Image): Terlampir di MLProject_Folder/Dockerhub.txt

Kontributor: Bunga Rasikhah Haya