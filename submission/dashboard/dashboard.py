import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import datetime
from PIL import Image

# Set theme
sns.set_theme(style='dark')

# Creating Helper Functions
def create_daily_users_df(df):
    return df.groupby('dateday').agg({
        'registered': 'sum',
        'casual': 'sum',
        'total': 'sum'
    }).reset_index()

def create_casreg_pie(df):
    return df[['casual', 'registered']].sum()

def create_grouped_df(df, group_col):
    return df.groupby(by=group_col).agg({
        'registered': 'sum',
        'casual': 'sum',
        'total': 'sum'
    }).sort_values(by='total', ascending=False)

# Load dataset
all_df = pd.read_csv('submission/dashboard/main_data.csv')

# Sorting & Changing Data Type
all_df['dateday'] = pd.to_datetime(all_df['dateday'])
all_df.sort_values(by='dateday', inplace=True)
all_df.reset_index(drop=True, inplace=True)

# Convert 'hour' to numeric format
all_df['hour'] = all_df['hour'].str.extract(r'(\d+)').astype(int)

# Sidebar for Dashboard
with st.sidebar:
  st.markdown('<div class="sidebar-content">', unsafe_allow_html=True)

    # Profile Header
    st.markdown('<div class="profile-header">PROFILE INFORMATION</div>', unsafe_allow_html=True)

    st.image(Image.open('submission/dashboard/user.png'), use_container_width=True, caption="Profile Picture", output_format="JPEG")


    # Profile Details
    st.markdown("""
        <div class="info">
            <div>👤 <span>:</span> Jihan Kusumawardhani</div>
            <div>📧 <span>:</span> jihankusumawwardhani@gmail.com</div>
            <div>🆔<span>:</span> jihankusumawardhani</div>
        </div>
    """, unsafe_allow_html=True)
    min_date, max_date = all_df['dateday'].min(), all_df['dateday'].max()
    start_date, end_date = st.date_input("Pilih Rentang Waktu", min_value=min_date, max_value=max_date, value=[min_date, max_date])
    
    st.markdown("""
    <style>
        .social-container {
            display: flex;
            justify-content: center;
            gap: 15px;
            margin-top: 15px;
        }
        .social-box {
            width: 70px;
            height: 70px;
            background-color: #f3f3f3;
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            box-shadow: 2px 2px 5px rgba(0,0,0,0.2);
        }
        .social-box img {
            width: 50px;
            height: 50px;
        }
    </style>

    <div class="social-container">
        <!-- LinkedIn -->
        <div class="social-box">
            <a href="https://www.linkedin.com/in/jihan-kusumawardhani-b43aaa343?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BziQ8j84iQy600UDtRm0t7Q%3D%3D" target="_blank">
                <img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" alt="LinkedIn">
            </a>
        </div>
        <!-- LinkedIn -->
        <div class="social-box">
            <a href="https://www.linkedin.com/in/jihan-kusumawardhani-b43aaa343?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BziQ8j84iQy600UDtRm0t7Q%3D%3D" target="_blank">
                <img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" alt="LinkedIn">
            </a>
        </div>
        
            
""", unsafe_allow_html=True)

# Menggunakan seluruh data tanpa filter tanggal
main_df = all_df.copy()

# Calling Helper Functions
daily_users_df = create_daily_users_df(main_df)
casreg_pie = create_casreg_pie(main_df)
sea_hour_df = create_grouped_df(main_df, 'season')
hr_hour_df = create_grouped_df(main_df, 'hour')
wd_hour_df = create_grouped_df(main_df, 'workingday')
weat_hour_df = create_grouped_df(main_df, 'weather')


# Making Title and Header for Dashboard
st.title('Analysis Bike Sharing Dataset 🚲')

st.markdown("""
    <h2 style="text-align: center;">✨ Welcome to my dashboard! ✨</h2>
""", unsafe_allow_html=True)


st.image(Image.open('submission/dashboard/bike-dataset.jpeg'), use_container_width=True, caption="Profile Picture", output_format="JPEG")


    min_date, max_date = all_df['dateday'].min(), all_df['dateday'].max()
    start_date, end_date = st.date_input("Pilih Rentang Waktu", min_value=min_date, max_value=max_date, value=[min_date, max_date])
    selected_weather = st.selectbox("Pilih kondisi cuaca:", all_df['weather'].unique())
    selected_workingday = st.radio("Hari kerja atau libur?", ['All', 0, 1])

    # Filter dataset based on date range, weather, and working day
    main_df = all_df[(all_df['dateday'] >= pd.Timestamp(start_date)) & (all_df['dateday'] <= pd.Timestamp(end_date))]
    if selected_weather != 'All':
        main_df = main_df[main_df['weather'] == selected_weather]
    if selected_workingday in [0, 1]:
        main_df = main_df[main_df['workingday'] == selected_workingday]

# Calculate total rentals
total_rentals = main_df['total'].sum()

# Dashboard Header
st.header("Bike Sharing Dashboard")
st.metric("Total Penyewaan", value=total_rentals)

# Pie chart pengguna casual vs registered
st.subheader("Perbandingan Pengguna Casual vs Registered")
casreg_pie = create_casreg_pie(main_df)
fig, ax = plt.subplots()
ax.pie(casreg_pie, labels=['Casual', 'Registered'], autopct='%1.1f%%', colors=['#FFBE98', '#A5DD9B'])
ax.set_title("Distribusi Pengguna")
st.pyplot(fig)

# Plot daily rental trends
st.subheader("Tren Penyewaan Harian")
plt.figure(figsize=(10, 5))
sns.lineplot(x='dateday', y='total', data=main_df, marker='o', color='#A5DD9B')
plt.xlabel("Tanggal")
plt.ylabel("Total Penyewaan")
st.pyplot(plt)

# Plot hourly rental distribution
st.subheader("Distribusi Penyewaan per Jam")
plt.figure(figsize=(10, 5))
sns.barplot(x='hour', y='total', data=main_df, palette='coolwarm')
plt.xlabel("Jam")
plt.ylabel("Total Penyewaan")
st.pyplot(plt)

# Tabs for additional analysis
st.title('Analysis Bike Sharing Dataset 🚲')
tab1, tab2, tab3, tab4 = st.tabs(["Overview", "Hourly Trends", "Weather Impact", "Seasonal Trends"])

with tab1:
    st.subheader("Overview of Bike Sharing Data")
    st.write("Dataset ini berisi informasi mengenai penyewaan sepeda berdasarkan hari dan jam.")

with tab2:
    st.subheader("Hourly Rental Trends")
    plt.figure(figsize=(10, 5))
    sns.lineplot(x='hour', y='total', data=main_df, color='#800020')
    plt.xlabel("Jam")
    plt.ylabel("Total Penyewaan")
    st.pyplot(plt)

with tab3:
    st.subheader("Impact of Weather on Rentals")
    plt.figure(figsize=(10, 5))
    sns.barplot(x='weather', y='total', data=main_df, palette='muted')
    plt.xlabel("Cuaca")
    plt.ylabel("Total Penyewaan")
    st.pyplot(plt)

with tab4:
    st.subheader("Seasonal Rental Trends")
    plt.figure(figsize=(10, 5))
    sns.barplot(x='season', y='total', data=main_df, palette='pastel')
    plt.xlabel("Musim")
    plt.ylabel("Total Penyewaan")
    st.pyplot(plt)
