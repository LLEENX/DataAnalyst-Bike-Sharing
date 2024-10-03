import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import numpy as np

# Set up the Streamlit page configuration
st.set_page_config(page_title="Dashboard Penggunaan Sepeda", layout="wide")

# Load dataset
@st.cache_data
def load_data():
    df_day = pd.read_csv("/dasboard/cleaned_days_df.csv")  # Dataset untuk data harian
    df_hour = pd.read_csv("/dasboard/cleaned_hours_df.csv")  # Dataset untuk data jam
    df_day['date'] = pd.to_datetime(df_day['date'])
    df_hour['date'] = pd.to_datetime(df_hour['date'])
    
    # Pastikan kolom 'hour' berada dalam format integer
    df_hour['hour'] = df_hour['hour'].astype(int)
    
    return df_day, df_hour

df_day, df_hour = load_data()

# Sidebar untuk filtering
min_date, max_date = df_day['date'].min(), df_day['date'].max()
start_date, end_date = st.sidebar.date_input("Pilih Rentang Tanggal", [min_date.date(), max_date.date()])

# Mengubah ke Timestamp untuk komperasi
start_date = pd.to_datetime(start_date)
end_date = pd.to_datetime(end_date)

# Filter data
if start_date == end_date:
    # Jika tanggal mulai dan tanggal akhir sama, filter untuk satu tanggal
    filtered_day_data = df_day[df_day['date'] == start_date]
    filtered_hour_data = df_hour[df_hour['date'] == start_date]
else:
    # Jika tanggal berbeda, filter untuk rentang tanggal
    filtered_day_data = df_day[(df_day['date'] >= start_date) & (df_day['date'] <= end_date)]
    filtered_hour_data = df_hour[(df_hour['date'] >= start_date) & (df_hour['date'] <= end_date)]

st.sidebar.markdown(
    """
    <style>
    .sidebar-image {
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 150px;
        border: 4px solid #ddd;  
        border-radius: 50%;     
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.sidebar.image("../image/photo.jpg", width=75, caption="By Rifal Ariya Yusuftrian", use_column_width=True) 

st.title("Dashboard Penggunaan Sepeda")
st.markdown("### Statistik Penggunaan Sepeda")

total_rides = filtered_day_data['count'].sum()
total_casual = filtered_day_data['casual'].sum()
total_registered = filtered_day_data['registered'].sum()

col1, col2, col3 = st.columns(3)
col1.metric("Total Rides", total_rides)
col2.metric("Total Casual Rides", total_casual)
col3.metric("Total Registered Rides", total_registered)

st.markdown("---")

# Visualisai untuk data peminjam perjam
hourly_data = filtered_hour_data.groupby('hour')['count'].sum().reset_index()
plt.figure(figsize=(10, 5))
sns.barplot(data=hourly_data, x='hour', y='count', palette='viridis')
plt.title('Jumlah Rides Berdasarkan Jam')
plt.xlabel('Jam')
plt.ylabel('Jumlah Rides')
st.pyplot(plt)

# Visualisasi untuk data weekday
days_users_df = filtered_day_data.groupby("weekday").agg({
    "casual": "sum",
    "registered": "sum",
    "count": "sum"
}).reset_index()

plt.figure(figsize=(12, 6))

# Lineplot for casual and registered users
sns.lineplot(x="weekday", y="casual", data=days_users_df, label='Casual', marker='o', color='blue', linewidth=2.5)
sns.lineplot(x="weekday", y="registered", data=days_users_df, label='Registered', marker='s', color='red', linewidth=2.5)

# Menyesuaikan sumbu x untuk menampilkan label hari dengan jelas
plt.xticks(np.arange(0, 7, 1), ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu'])

plt.xlabel("Hari", fontsize=14)
plt.ylabel("Total Rides", fontsize=14)
plt.title("Jumlah Rides Berdasarkan Hari", fontsize=16)

plt.axvline(x=1, color='gray', linestyle='--', label='Rata-rata Peminjaman')
plt.axvline(x=5, color='gray', linestyle='--')

plt.legend(loc='upper right', fontsize=14)
plt.grid(True)  
plt.tight_layout()
st.pyplot(plt)

# Visualisai untuk data peminjam perbulan
monthly_data = filtered_day_data.resample('M', on='date').sum().reset_index()
plt.figure(figsize=(10, 5))
sns.lineplot(data=monthly_data, x='date', y='count', marker='o')
plt.title('Jumlah Rides Bulanan')
plt.xlabel('Bulan')
plt.ylabel('Jumlah Rides')
st.pyplot(plt)

st.markdown("---")

# Visualisai untuk data seasonal
seasonly_df = filtered_day_data.groupby("season").agg({
    "casual": "sum",
    "registered": "sum",
    "count": "sum"
}).reset_index().sort_values(by='count')

plt.figure(figsize=(10, 6))
sns.barplot(
    x="season", 
    y="count", 
    data=seasonly_df
)
plt.xlabel("Musim")
plt.ylabel("Total Rides")
plt.title("Jumlah Rides Berdasarkan Musim", size=12)
st.pyplot(plt)

st.markdown("---")

hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
st.markdown(hide_st_style, unsafe_allow_html=True)
