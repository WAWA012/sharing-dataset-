import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set_theme(style='dark')

# Fungsi-fungsi analisis
def total_rent_by_hours(df):
    return df.groupby(by="hour").agg({"total_count": ["sum"]})

def analysis_rent_by_hours(df):
    return df.groupby("hour").total_count.mean().sort_values(ascending=False).reset_index()

def rent_by_season(df):
    return df.groupby("season").total_count.sum().sort_values(ascending=False).reset_index()

def rent_by_weather(df):
    return df.groupby("weather").total_count.nunique().sort_values(ascending=False).reset_index()

# Load dataset
dataset_bike = pd.read_csv("submission/dashboard/main_data.csv")

# Pastikan kolom tersedia
if 'dateday' in dataset_bike.columns:
    dataset_bike['dateday'] = pd.to_datetime(dataset_bike['dateday'])  # Ubah ke datetime
    dataset_bike.sort_values(by="dateday", inplace=True)
    dataset_bike.reset_index(drop=True, inplace=True)

    min_date = dataset_bike['dateday'].min()
    max_date = dataset_bike['dateday'].max()

    with st.sidebar:
        # Logo
        st.image("https://images.unsplash.com/photo-1496147433903-1e62fdb6f4be?q=80&w=1421&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D")

        # Rentang tanggal
        start_date, end_date = st.date_input(
            label='Rentang tanggal',
            min_value=min_date,
            max_value=max_date,
            value=[min_date, max_date]
        )

        df_by_days = dataset_bike[(dataset_bike['dateday'] >= str(start_date)) & 
                                  (dataset_bike['dateday'] <= str(end_date))]

        df_rent_by_hours = total_rent_by_hours(df_by_days)
        df_analysis_rent_hours = analysis_rent_by_hours(df_by_days)
        df_rent_by_season = rent_by_season(df_by_days)
        df_rent_by_weather = rent_by_weather(df_by_days)
    
    # Dashboard
    st.header('Bike Sharing')
    st.subheader('Jumlah Penyewaan Sepeda Harian')

    total_rent = df_rent_by_hours.total_count.sum()
    st.metric("Jumlah Penyewaan", value=total_rent)
    
    # Jam dengan rata-rata penyewaan tertinggi
    st.subheader("Jam dengan Rata-rata Penyewaan Sepeda Terbanyak")
    colors = ['#A5DD9B', '#C5EBAA', '#F6F193', '#F2C18D']
    
    plt.figure(figsize=(10, 5))
    sns.barplot(
        y="total_count", 
        x="hour",
        data=df_analysis_rent_hours.sort_values(by="total_count", ascending=False).head(3),
        palette=colors
    )
    plt.ylabel(None)
    plt.xlabel(None)
    plt.tick_params(axis='x', labelsize=12)
    st.pyplot(plt)

    # Penyewaan berdasarkan musim
    st.subheader("Penyewaan Sepeda Berdasarkan Musim")
    colors = ['#FFBE98', '#FEECE2', '#F7DED0', '#E2BFB3']
    
    plt.figure(figsize=(10, 5))
    sns.barplot(
        y="total_count", 
        x="season",
        data=df_rent_by_season.sort_values(by="total_count", ascending=False),
        palette=colors
    )
    plt.ylabel(None)
    plt.xlabel(None)
    plt.tick_params(axis='x', labelsize=12)
    plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
    st.pyplot(plt)

    # Penyewaan berdasarkan cuaca
    st.subheader("Jumlah Pelanggan Berdasarkan Kondisi Cuaca")
    colors = ['#FFBE98', '#FEECE2', '#F7DED0', '#E2BFB3']
    
    plt.figure(figsize=(10, 5))
    sns.barplot(
        y="total_count", 
        x="weather",
        data=df_rent_by_weather.sort_values(by="total_count", ascending=False),
        palette=colors
    )
    plt.ylabel(None)
    plt.xlabel(None)
    plt.tick_params(axis='x', labelsize=12)
    plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
    st.pyplot(plt)

else:
    st.error("Kolom 'dateday' tidak ditemukan dalam dataset! Pastikan nama kolom sudah benar.")
    st.write("Kolom yang tersedia:", dataset_bike.columns)
