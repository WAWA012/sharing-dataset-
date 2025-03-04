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
import streamlit as st
import pandas as pd
from PIL import Image

# Custom CSS untuk styling
st.markdown("""
   <style>
        .profile-header {
            font-size: 24px;
            font-weight: bold;
            margin-bottom: 15px;
            padding-bottom: 8px;
            border-bottom: 2px solid #555;
            color: white;
            text-align: center;
            width: 100%;
        }
        .info {
            text-align: left;
            font-size: 16px;
            margin-top: 10px;
            color: white;
        }
        .info div {
            margin-bottom: 8px;
        }
        .info span {
            font-weight: bold;
            color: white;
        }
        .sidebar-img {
            border-radius: 10px;
            display: block;
            margin: auto;
            width: 100%;
            max-width: 200px;
        }
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
            border-radius: 10px;
            box-shadow: 2px 2px 5px rgba(0,0,0,0.2);
        }
        .social-box img {
            width: 40px;
            height: 40px;
        }
        .social-box a {
            display: flex;
            align-items: center;
            justify-content: center;
            width: 100%;
            height: 100%;
        }
    </style>
""", unsafe_allow_html=True)

# Load dataset
all_df = pd.read_csv("submission/dashboard/main_data.csv")

# Convert 'dateday' to datetime
all_df['dateday'] = pd.to_datetime(all_df['dateday'])

# Sidebar for Dashboard
with st.sidebar:
    st.markdown('<div class="profile-header">PROFILE INFORMATION</div>', unsafe_allow_html=True)
    
    # Profile Picture
    st.image(Image.open("submission/dashboard/user.png"), caption="Profile Picture")
   
    # Profile Details
    st.markdown("""
        <div class="info">
            <div>👤 <span>:</span> Jihan Kusumawardhani</div>
            <div>📧 <span>:</span> <a href="mailto:jihankusumawwardhani@gmail.com" style="color:white; text-decoration:none;">jihankusumawwardhani@gmail.com</a></div>
            <div>🆔 <span>:</span> jihankusumawardhani</div>
        </div>
    """, unsafe_allow_html=True)

    # Rentang Waktu
    min_date, max_date = all_df['dateday'].min(), all_df['dateday'].max()
    start_date, end_date = st.date_input("Pilih Rentang Waktu", min_value=min_date, max_value=max_date, value=[min_date, max_date])
    
    # Filter berdasarkan cuaca
    selected_weather = st.selectbox("Pilih kondisi cuaca:", ['All'] + list(all_df['weather'].unique()))
    
    # Filter dataset
    main_df = all_df[(all_df['dateday'] >= pd.Timestamp(start_date)) & (all_df['dateday'] <= pd.Timestamp(end_date))]
    if selected_weather != 'All':
        main_df = main_df[main_df['weather'] == selected_weather]

    # Sosial Media
    st.markdown("""
    <div class="social-container">
        <!-- LinkedIn -->
        <div class="social-box">
            <a href="https://www.linkedin.com/in/jihan-kusumawardhani-b43aaa343" target="_blank">
                <img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" alt="LinkedIn">
            </a>
        </div>
        <!-- GitHub -->
        <div class="social-box">
            <a href="https://github.com/WAWA012" target="_blank">
                <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" alt="GitHub">
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
# Calculate total rentals
total_rentals = main_df['total'].sum()

# Main title
st.markdown("""
    <h2 style="text-align: center; color: white;">📊 Analysis Bike Sharing Dataset 🚲</h2>
""", unsafe_allow_html=True)

# Display profile image
st.image(Image.open('submission/dashboard/bike-dataset.jpeg'), use_container_width=True, caption="Bike Sharing Dataset", output_format="JPEG")
# Show total rentals metric in a more structured layout

st.markdown(
    f"""
    <div style="display: flex; align-items: center; justify-content: center;">
        <h3 style="margin-right: 10px;">Total Penyewaan:</h3>
        <h3 style="color: white; margin: 0;">{total_rentals}</h3>
    </div>
    """,
    unsafe_allow_html=True
)



# Layout for visualizations
col1, col2 = st.columns([1, 2])

# Pie chart for user distribution
with col1:
    st.markdown("<h4>📊 Perbandingan Pengguna Casual vs Registered</h4>", unsafe_allow_html=True)
    casreg_pie = create_casreg_pie(main_df)
    fig, ax = plt.subplots(figsize=(4, 4))  # Perbesar ukuran figure biar gak terlalu kecil
    ax.pie(casreg_pie, labels=['Casual', 'Registered'], autopct='%1.1f%%', colors=['#800020', '#F5F5DC'])
    st.pyplot(fig)

with col2:
    st.subheader("📈 Tren Penyewaan Harian")
    plt.figure(figsize=(8, 4))
    sns.lineplot(x='dateday', y='total', data=main_df, marker='o', color='#800020')
    plt.xlabel("Tanggal")
    plt.ylabel("Total Penyewaan")
    plt.grid(alpha=0.1)
    st.pyplot(plt)

# Distribusi Penyewaan per Jam
st.subheader("⏳ Distribusi Penyewaan per Jam")
plt.figure(figsize=(12, 5))
sns.barplot(x='hour', y='total', data=main_df, palette=['#800020', '#A52A2A', '#D2691E', '#F4A460'])
plt.xlabel("Jam")
plt.ylabel("Total Penyewaan")
plt.xticks(rotation=45)  # Putar label supaya lebih terbaca
plt.grid(alpha=0.3)
st.pyplot(plt)

# Footer Welcome Message
st.markdown("""
    <div style="text-align: center; background-color: #800020; padding: 10px; border-radius: 10px; color: white;">
        <h2>✨ Welcome to my dashboard! ✨</h2>
    </div>
""", unsafe_allow_html=True)

tab1, tab2, tab3, tab4, tab5 = st.tabs(["The Rationale Behind the Dashboard","Overview of the Bike Sharing Dataset", "Hourly Trends", "Weather Impact", "Seasonal Trends"]) 

with tab1:
    st.markdown("""
    <style>
        .justify-text {
            text-align: justify;
            text-justify: inter-word;
            font-size: 20px;
            line-height: 1.6;
            color: white; /* Ubah warna teks jadi putih */
        }
        .centered-header {
            text-align: center;
            font-size: 24px;
            font-weight: bold;
            color: white; /* Warna putih */
        }
    </style>
    """, unsafe_allow_html=True)


    # Konten Indonesia
    st.markdown("""
        <p class="justify-text">
        <strong>Indonesia:</strong> <br><br>
        Tujuan dari pengembangan dashboard proyek akhir untuk analisis dataset sepeda ini adalah untuk memenuhi persyaratan proyek akhir dalam program pembelajaran Analisis Data dari Dicoding.  
        Dashboard ini berfungsi sebagai platform komprehensif untuk menyajikan wawasan utama, tren, dan pola yang diperoleh dari dataset, memastikan pendekatan yang terstruktur dan berbasis data dalam pengambilan keputusan analitis.  
        Dengan memanfaatkan berbagai teknik visualisasi data, dashboard ini secara efektif mengkomunikasikan temuan, memungkinkan pemahaman yang lebih mendalam dan interpretasi dataset yang lebih akurat.  
        Selain itu, proyek ini bertujuan untuk meningkatkan keterampilan dalam pemrosesan data, visualisasi, dan interpretasi, memperkuat kemampuan analitis yang penting dalam pemecahan masalah berbasis data di dunia nyata.
        </p>
    """, unsafe_allow_html=True)

    # Garis pembatas
    st.markdown("##### ____________________________________________________________________")

    # Konten English
    st.markdown("""
        <p class="justify-text">
        <strong>English:</strong> <br><br>
        The purpose of developing this final project dashboard for the Bike dataset analysis is to fulfill the requirements of the final project in the Data Analysis learning program from Dicoding.  
        This dashboard serves as a comprehensive platform to present key insights, trends, and patterns derived from the dataset, ensuring a structured and data-driven approach to analytical decision-making.  
        By utilizing various data visualization techniques, the dashboard effectively communicates findings, enabling deeper understanding and more informed interpretations of the dataset.  
        Additionally, this project aims to enhance proficiency in data processing, visualization, and interpretation, reinforcing analytical skills essential for real-world data-driven problem-solving.
        </p>
    """, unsafe_allow_html=True)

with tab2:
    # CSS untuk justify text & center subheader
    st.markdown("""
        <style>
            .justify-text {
                text-align: justify;
                text-justify: inter-word;
                font-size: 16px;
                line-height: 1.6;
                color: white; /* Ubah warna teks jadi putih */
            }
            .centered-header {
                text-align: center;
                font-size: 24px;
                font-weight: bold;
                color: white; /* Bisa diganti sesuai tema */
            }
        </style>
    """, unsafe_allow_html=True)

    # Konten Indonesia
    st.markdown("""
        <p class="justify-text">
        <strong>Indonesia:</strong> <br><br>
        Dataset ini menyediakan catatan rinci tentang jumlah penggunaan sepeda sewaan, baik secara per jam maupun harian, dalam sistem Capital Bike Share.  
        Data ini mencakup periode dari tahun 2011 hingga 2012 dan menyertakan informasi kontekstual yang relevan, seperti kondisi cuaca dan variasi musiman,  
        yang dapat memengaruhi pola penyewaan sepeda.
        </p>
    """, unsafe_allow_html=True)

    # Garis pembatas
    st.markdown("##### ____________________________________________________________________")

    # Konten English
    st.markdown("""
        <p class="justify-text">
        <strong>English:</strong> <br><br>
        This dataset provides detailed records of the number of rental bike usages, both on an hourly and daily basis, within the Capital Bike Share system.  
        The data spans from 2011 to 2012 and includes relevant contextual information, such as weather conditions and seasonal variations,  
        which may influence bike rental patterns.
        </p>
    """, unsafe_allow_html=True)

with tab3:
    st.subheader("Hourly Rental Trends")
    plt.figure(figsize=(10, 5))
    sns.lineplot(x='hour', y='total', data=main_df, color='#800020', linewidth=2, marker='o', markerfacecolor='#800020')
    plt.xlabel("Jam", fontsize=12, fontweight='bold', color="#800020")
    plt.ylabel("Total Penyewaan", fontsize=12, fontweight='bold', color="#800020")
    st.pyplot(plt)

with tab4:
    st.subheader("Impact of Weather on Rentals")
    plt.figure(figsize=(10, 5))
    sns.barplot(x='weather', y='total', data=main_df, palette=['#800020', '#A52A2A', '#D2691E', '#E97451'])
    plt.xlabel("Cuaca", fontsize=12, fontweight='bold', color="#800020")
    plt.ylabel("Total Penyewaan", fontsize=12, fontweight='bold', color="#800020")
    st.pyplot(plt)

with tab5:
    st.subheader("Seasonal Rental Trends")
    plt.figure(figsize=(10, 5))
    sns.barplot(x='season', y='total', data=main_df, palette=['#800020', '#B22222', '#DC143C', '#E97451'])
    plt.xlabel("Musim", fontsize=12, fontweight='bold', color="#800020")
    plt.ylabel("Total Penyewaan", fontsize=12, fontweight='bold', color="#800020")
    st.pyplot(plt)
    # Making a Caption

st.caption("© 2025 Jihan Kusumawardhani. All Rights Reserved.")
