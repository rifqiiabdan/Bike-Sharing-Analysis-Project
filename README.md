# Bike Sharing Analysis Dashboard

Dashboard ini dibuat untuk menganalisis dataset **Bike Sharing** menggunakan **Streamlit**. Dashboard menampilkan visualisasi data dan insight terkait pola penyewaan sepeda berdasarkan musim, bulan, dan kondisi cuaca.

## Fitur
- **Filter interaktif**: Pengguna dapat memilih tahun dan musim untuk melihat data yang difilter.
- **Visualisasi interaktif**:
  - Total penyewaan sepeda per musim.
  - Tren penyewaan sepeda per bulan.
- **Kesimpulan analisis**: Ringkasan insight dan rekomendasi bisnis.

## Cara Menjalankan Dashboard

### Prasyarat
- Python 3.8+
- Virtual environment (opsional)

## Cara menjalankan program
**Buat venv terlebih dahulu dan aktifkan**
```bash
python -m venv .venv
```

**Install Library yang dibutuhkan dan lakukan running program di mode aktif venv**
```bash
pip install -r requirements.txt
cd dashboard
streamlit run app.py
 ``` 
