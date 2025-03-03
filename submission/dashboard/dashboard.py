import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
sns.set_theme(style='dark')

def total_rent_by_hours(df):
    rent_by_hour = df.groupby(by="hour").agg({"total_count":["sum"]})
    return rent_by_hour

def analysis_rent_by_hours(df):
    avg_rent = df.groupby("hour").total_count.mean().sort_values(ascending=False).reset_index()
    return avg_rent
def rent_by_season(df):
    rent_by_season = df.groupby("season").total_count.sum().sort_values(ascending=False).reset_index()
    return rent_by_season

def rent_by_weather(df):
    rent_by_weather = df.groupby("weather").total_count.nunique().sort_values(ascending=False).reset_index()
    return rent_by_weather

dataset_bike = pd.read_csv("submission/dashboard/main_data.csv")
datetime_columns = ['date']
dataset_bike.sort_values(by="date", inplace=True)
dataset_bike.reset_index(inplace=True)

for column in datetime_columns:
    dataset_bike[column] = pd.to_datetime(dataset_bike['date'])

min_date = dataset_bike['date'].min()
max_date = dataset_bike['date'].max()

with st.sidebar:
    #logo company
    st.image("https://images.unsplash.com/photo-1496147433903-1e62fdb6f4be?q=80&w=1421&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D")
    #Mengambil start date dan end date
    start_date, end_date = st.date_input(
        label='Rentang tanggal',
        min_value=min_date,
        max_value=max_date,
        value=[min_date,max_date]
    )
    df_by_days = dataset_bike[(dataset_bike['date'] >= str(start_date)) & 
                              (dataset_bike['date'] <= str(end_date))]
    df_rent_by_hours = total_rent_by_hours(df_by_days)
    df_analysis_rent_hours = analysis_rent_by_hours(df_by_days)
    df_rent_by_season = rent_by_season(df_by_days)
    df_rent_by_weather = rent_by_weather(df_by_days)
    
st.header('Bike Sharing')
st.subheader('Jumlah penyewaan sepeda harian')
total_rent = df_rent_by_hours.total_count.sum()
st.metric("Jumah penyewaan ", value=total_rent)
        
st.subheader("Jam dengan rata-rata penyewaan sepeda terbanyak")
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

st.subheader("Penyewaan Sepeda Berdasarkan musim")
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

st.subheader("Jumlah pelanggan berdasarkan kondisi cuaca")
df_rent_by_weather
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
