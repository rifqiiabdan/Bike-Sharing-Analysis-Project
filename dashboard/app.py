import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Judul Dashboard
st.set_page_config(page_title="Bike Sharing Analysis", layout="wide")
st.title("Bike Sharing Dataset Analysis Dashboard")

# Fungsi untuk memuat data
@st.cache_data  # Cache data untuk meningkatkan performa
def load_data():
    # Path ke file day.csv (pastikan path sesuai dengan struktur folder Anda)
    data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/day.csv'))
    day_df = pd.read_csv(data_path)
    
    # Konversi kolom 'dteday' ke tipe datetime
    day_df['dteday'] = pd.to_datetime(day_df['dteday'])
    
    # Mapping nilai kategorikal
    season_map = {1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'}
    weather_map = {1: 'Clear', 2: 'Mist', 3: 'Light Rain', 4: 'Heavy Rain'}
    
    day_df['season'] = day_df['season'].map(season_map)
    day_df['weathersit'] = day_df['weathersit'].map(weather_map)
    
    return day_df

# Memuat data
df = load_data()

# Sidebar untuk filter data
st.sidebar.header("Filter Data")
selected_year = st.sidebar.selectbox("Pilih Tahun", df['dteday'].dt.year.unique())
selected_season = st.sidebar.selectbox("Pilih Musim", df['season'].unique())

# Filter data berdasarkan pilihan di sidebar
filtered_df = df[
    (df['dteday'].dt.year == selected_year) &
    (df['season'] == selected_season)
]

# Tampilkan data yang difilter
st.subheader("Data yang Difilter")
st.dataframe(filtered_df)

# Visualisasi 1: Penyewaan Sepeda per Musim
st.subheader("Rata-Rata Penyewaan Sepeda per Musim")
seasonal_avg = df.groupby('season')['cnt'].mean().reset_index()

fig1, ax1 = plt.subplots(figsize=(10, 6))
sns.barplot(x='season', y='cnt', data=seasonal_avg, ax=ax1, palette='viridis')
plt.title('Rata-Rata Penyewaan Sepeda per Musim')
plt.xlabel('Musim')
plt.ylabel('Rata-Rata Penyewaan')
st.pyplot(fig1)

# Visualisasi 2: Penyewaan Sepeda per Kondisi Cuaca
st.subheader("Rata-Rata Penyewaan Sepeda per Kondisi Cuaca")
weather_avg = df.groupby('weathersit')['cnt'].mean().reset_index()

fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.barplot(x='weathersit', y='cnt', data=weather_avg, ax=ax2, palette='coolwarm')
plt.title('Rata-Rata Penyewaan Sepeda per Kondisi Cuaca')
plt.xlabel('Kondisi Cuaca')
plt.ylabel('Rata-Rata Penyewaan')
st.pyplot(fig2)

# Visualisasi 3: Tren Penyewaan Sepeda per Bulan
st.subheader("Tren Penyewaan Sepeda per Bulan")
df['month'] = df['dteday'].dt.month_name()
monthly_trend = df.groupby('month')['cnt'].sum().reset_index()

# Urutkan bulan secara kronologis
month_order = [
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'
]
monthly_trend['month'] = pd.Categorical(monthly_trend['month'], categories=month_order, ordered=True)
monthly_trend = monthly_trend.sort_values('month')

fig3, ax3 = plt.subplots(figsize=(12, 6))
sns.lineplot(x='month', y='cnt', data=monthly_trend, marker='o', ax=ax3)
plt.title('Tren Penyewaan Sepeda per Bulan')
plt.xlabel('Bulan')
plt.ylabel('Total Penyewaan')
plt.xticks(rotation=45)
st.pyplot(fig3)

# Kesimpulan
st.subheader("Kesimpulan")
st.write("""
1. **Pengaruh Musim**: Penyewaan sepeda tertinggi terjadi pada musim **Fall (Gugur)** dan terendah pada musim **Spring (Semi)**.
2. **Pengaruh Cuaca**: Penyewaan sepeda paling tinggi saat cuaca **Clear (Cerah)** dan menurun signifikan saat cuaca **Heavy Rain (Hujan Lebat)**.
3. **Tren Bulanan**: Penyewaan sepeda cenderung meningkat selama musim panas (Juni, Juli, Agustus) dan menurun selama musim dingin (Desember, Januari, Februari).
""")