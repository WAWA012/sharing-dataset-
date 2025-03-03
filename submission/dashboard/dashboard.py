import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from PIL import Image

import pandas as pd
import streamlit as st
from PIL import Image

import pandas as pd
import streamlit as st
from PIL import Image

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

# Load File as a DataFrame
all_df = pd.read_csv('submission/dashboard/main_data.csv')

# Sorting & Changing Data Type
all_df['dateday'] = pd.to_datetime(all_df['dateday'])
all_df.sort_values(by='dateday', inplace=True)
all_df.reset_index(drop=True, inplace=True)
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
            display: flex;
            justify-content: center;
            align-items: center;
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
        .social-box {
            margin-top: 15px;
            padding: 12px;
            border-radius: 8px;
            text-align: center;
            font-weight: bold;
            font-size: 16px;
        }
        .linkedin-box {
            background-color: #0077B5;
        }
        .github-box {
            background-color: #24292E;
        }
        .social-box a {
            color: white;
            text-decoration: none;
            display: block;
        }
        .social-box a:hover {
            opacity: 0.8;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar for Dashboard
with st.sidebar:
    st.markdown('<div class="sidebar-content">', unsafe_allow_html=True)

    # Profile Header
    st.markdown('<div class="profile-header">PROFILE INFORMATION</div>', unsafe_allow_html=True)

    # Profile Picture
    st.image(Image.open('user.png'), use_container_width=True, caption="Profile Picture", output_format="JPEG")

    # Profile Details
    st.markdown("""
        <div class="info">
            <div>👤 <span>:</span> Jihan Kusumawardhani</div>
            <div>📧 <span>:</span> jihankusumawwardhani@gmail.com</div>
            <div>🆔<span>:</span> jihankusumawardhani</div>
        </div>
    """, unsafe_allow_html=True)

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


st.image(Image.open('bike-dataset.jpeg'), width=700) 

# Making Tabs for Dashboard
tab1, tab2, tab3, tab4, tab5, tab6, tab7= st.tabs([
    'The Rationale Behind the Dashboard', 'Overview of the Bike Sharing Dataset','What inquiries need to be addressed?', 'In-Depth Analytical Explanation', 'Inquiry 1', 'Inquiry 2', 'Inquiry 3'])

with tab1:
            # CSS untuk justify text & center subheader
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

# Subheader di tengah dengan warna putih
    st.markdown("<p class='centered-header'>The Rationale Behind the Dashboard</p>", unsafe_allow_html=True)

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
            }
            .centered-header {
                text-align: center;
                font-size: 24px;
                font-weight: bold;
                color: white; /* Bisa diganti sesuai tema */
            }
        </style>
    """, unsafe_allow_html=True)

    # Subheader di tengah
    st.markdown("<p class='centered-header'>Overview of the Bike Sharing Dataset</p>", unsafe_allow_html=True)

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
    # CSS untuk justify text, center subheader, dan sejajarkan nomor daftar
    st.markdown("""
        <style>
            .justify-text {
                text-align: justify;
                text-justify: inter-word;
                font-size: 16px;
                line-height: 1.8;
            }
            .centered-header {
                text-align: center;
                font-size: 24px;
                font-weight: bold;
                color: white; /* Bisa diganti sesuai tema */
                margin-bottom: 20px;
            }
            .numbered-list {
                text-align: justify;
                padding-left: 5px;
                margin-left: 5px;
                list-style-position: outside; /* Biar nomor tetap sejajar kiri */
            }
        </style>
    """, unsafe_allow_html=True)

    # Subheader di tengah
    st.markdown("<p class='centered-header'>What Inquiries Need to Be Addressed?</p>", unsafe_allow_html=True)

    # Konten Indonesia
    st.markdown("""
    <p class="justify-text"><strong>Indonesia:</strong></p>
    <ol class="justify-text numbered-list">
            <li>Bagaimana perbedaan antara pengguna yang menggunakan layanan bike sharing secara kasual tanpa registrasi dengan mereka yang telah mendaftar sebagai anggota tetap dalam sistem tersebut?</li>
            <li>Pada jam berapa dalam sehari tingkat penggunaan layanan bike sharing mencapai puncak tertinggi, dan pada jam berapa penggunaan tersebut berada pada titik terendah?
</li>
            <li>Bagaimana perbedaan dalam pola penggunaan layanan bike sharing ketika dihadapkan pada empat kondisi cuaca yang berbeda, dan sejauh mana faktor cuaca memengaruhi tingkat penggunaannya?
</li>
        </ol>    
    """, unsafe_allow_html=True)

    # Garis pembatas
    st.markdown("##### ____________________________________________________________________")

    # Konten English
    st.markdown("""
        <p class="justify-text"><strong>English:</strong></p>
        <ol class="justify-text numbered-list">
            <li>What are the key differences between casual users who utilize bike-sharing services without registration and those who have enrolled as permanent members within the system?</li>
            <li>At what time of day does bike-sharing usage peak, and when does it reach its lowest point?</li>
            <li>How do bike-sharing usage patterns vary across four different weather conditions, and to what extent does weather influence the overall usage rate?</li>
        </ol>
    """, unsafe_allow_html=True)



with tab4:
    # CSS untuk justify text & center subheader
    st.markdown("""
    <style>
        .justify-text {
            text-align: justify;
            text-justify: inter-word;
            font-size: 16px;
            line-height: 1.6;
        }
        .centered-header {
            text-align: center;
            font-size: 24px;
            font-weight: bold;
           color: white; /* Bisa diganti sesuai tema */
        }
    </style>
""", unsafe_allow_html=True)

# Subheader di tengah
    st.markdown("<p class='centered-header'>Daily Users</p>", unsafe_allow_html=True)

# Konten Indonesia
    st.markdown("""
        <p class="justify-text"> 
        <strong>Indonesia:</strong> <br><br>
        Dataset ini memberikan wawasan tentang jumlah pengguna yang menggunakan layanan berbagi sepeda setiap hari.  
        Berdasarkan analisis, pengguna dikategorikan ke dalam dua kelompok berbeda:
        </p>
        
        <ul class="justify-text">
            <li><strong>Pengguna Terdaftar:</strong> Sebanyak 2.672.662 individu telah menggunakan layanan ini dengan akun terdaftar,  
            menunjukkan ketergantungan yang kuat pada pengguna reguler yang memiliki keanggotaan tetap.</li>
            <li><strong>Pengguna Kasual:</strong> Dataset mencatat 620.017 pengguna kasual, yaitu mereka yang tidak memiliki akun terdaftar  
            tetapi tetap menggunakan layanan ini sesekali.</li>
        </ul>
        
        <p class="justify-text">
        Secara keseluruhan, jumlah kumulatif pengguna—baik terdaftar maupun kasual—mencapai 3.292.679, yang menyoroti skala penggunaan layanan berbagi sepeda dalam periode waktu yang diamati.
        </p>
    """, unsafe_allow_html=True)

    # Garis pembatas
    st.markdown("##### ____________________________________________________________________")

    # Konten English
    st.markdown("""
        <p class="justify-text">
        <strong>English:</strong> <br><br>
        The dataset provides insights into the number of users utilizing the bike-sharing service on a daily basis.  
        Based on the analysis, the users are categorized into two distinct groups:
        </p>
        
        <ul class="justify-text">
            <li><strong>Registered Users:</strong> A total of 2,672,662 individuals have used the service under registered accounts,  
            indicating a strong reliance on regular users who have an established membership.</li>
            <li><strong>Casual Users:</strong> The dataset records 620,017 casual users, representing those who do not have a registered account  
            but still engage with the service occasionally.</li>
        </ul>
        
        <p class="justify-text">
        In total, the cumulative number of users—both registered and casual—reaches 3,292,679,  
        highlighting the overall scale of bike-sharing usage within the observed timeframe.
        </p>
    """, unsafe_allow_html=True)

    # Garis pembatas
    st.markdown("##### ____________________________________________________________________")

    # Metrics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Registered Users:", value=daily_users_df.registered.sum())
    with col2:
        st.metric("Casual Users:", value=daily_users_df.casual.sum())
    with col3:
        st.metric("Total Users:", value=daily_users_df.total.sum())

    # Scatter Plot Daily Users
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.scatter(daily_users_df["dateday"], daily_users_df["total"], color="#800020")  # Burgundy
    st.pyplot(fig)


with tab5:
    st.markdown("""
        <p class="justify-text"><strong>Indonesia:</strong></p>
        <ol class="justify-text numbered-list">
                <li>Bagaimana perbedaan antara pengguna yang menggunakan layanan bike sharing secara kasual tanpa registrasi dengan mereka yang telah mendaftar sebagai anggota tetap dalam sistem tersebut?</li>
            </ol>  
        <ul class="justify-text numbered-list">
                <li>Jumlah pengguna yang telah melakukan pendaftaran sebagai member atau pengguna terdaftar jauh lebih tinggi dibandingkan dengan jumlah pengguna yang hanya menggunakan layanan secara kasual tanpa registrasi. Persentase pengguna terdaftar mencapai 81.2%, sedangkan pengguna kasual hanya mencakup 18.8% dari total pengguna.</li>
            </ul>    
        """, unsafe_allow_html=True)

        # Garis pembatas
    st.markdown("##### ____________________________________________________________________")

        # Konten English
    st.markdown("""
            <p class="justify-text"><strong>English:</strong></p>
            <ol class="justify-text numbered-list">
                <li>What are the key differences between casual users who utilize bike-sharing services without registration and those who have enrolled as permanent members within the system?</li>
            </ol>
        <ul class="justify-text numbered-list">
                <li>The number of users who have registered as members or verified users is significantly higher compared to those who access the services casually without registration. Registered users account for 81.2% of the total user base, while casual users make up only 18.8%. </li>
            </ul> 
        """, unsafe_allow_html=True)

            # Garis pembatas
    st.markdown("##### ____________________________________________________________________")
    


    colors = ['#800020', '#F5F5DC']  # Burgundy & Beige

    # Buat pie chart
    fig, ax = plt.subplots(figsize=(5, 5))
    wedges, texts, autotexts = ax.pie(
        casreg_pie.values, labels=['CASUAL', 'REGISTERED'], autopct='%1.1f%%', colors=colors,
        startangle=90, wedgeprops={'edgecolor': 'black'}
    )

    # Atur warna teks persentase
    autotexts[0].set_color('#F5F5DC')  # Casual → Beige
    autotexts[1].set_color('#800020')  # Registered → Burgundy
    # Atur warna label (User Type)
    for text in texts:
        text.set_color("black")

    # Tambahkan judul
    ax.set_title("Casual vs Registered Users", fontsize=12, fontweight='bold', color="#800020")

    # Tampilkan plot di Streamlit
    st.pyplot(fig)


with tab6:
    
    st.markdown("""
    <p class="justify-text"><strong>Indonesia:</strong></p>
    <ol class="justify-text numbered-list">
            <li>Pada jam berapa dalam sehari tingkat penggunaan layanan bike sharing mencapai puncak tertinggi, dan pada jam berapa penggunaan tersebut berada pada titik terendah?</li>
        </ol>  
    <ul class="justify-text numbered-list">
            <li>Pola penggunaan layanan Bike Sharing menunjukkan bahwa pada hari kerja, puncak aktivitas peminjaman sepeda terjadi pada pukul 17.00 atau jam 5 sore. Hal ini kemungkinan besar disebabkan oleh banyaknya pekerja yang pulang dari kantor pada jam tersebut.</li>
        </ul>    
    """, unsafe_allow_html=True)

    # Garis pembatas
    st.markdown("##### ____________________________________________________________________")

    # Konten English
    st.markdown("""
        <p class="justify-text"><strong>English:</strong></p>
        <ol class="justify-text numbered-list">
            <li>What are the key differences between casual users who utilize bike-sharing services without registration and those who have enrolled as permanent members within the system?</li>
        </ol>
    <ul class="justify-text numbered-list">
            <li>The usage pattern of Bike Sharing services indicates that on weekdays, peak bike rentals occur at 5:00 PM, likely driven by the high number of employees commuting home from work.</li>
        </ul> 
    """, unsafe_allow_html=True)

        # Garis pembatas
    st.markdown("##### ____________________________________________________________________")

    # Setup figure
    fig, ax = plt.subplots(figsize=(20, 10))
    sns.despine(fig)  # Menghapus garis tepi agar lebih bersih
    sns.set_style('whitegrid')  # Set gaya grid putih

    # Plot line chart
    sns.lineplot(
    data=hr_hour_df, x='hour', y='total', color='#800020', linewidth=2,
    marker='o', markerfacecolor='#F5F5DC', markeredgecolor='black'
    )

    # Styling
    plt.title('Penggunaan Bike Sharing Tertinggi dan Terendah Berdasarkan Waktu (Jam)', 
    fontsize=12, fontweight='bold', color="#800020")
    plt.xlabel(None)
    plt.ylabel(None)

    # Tampilkan di Streamlit
    st.pyplot(fig)


with tab7:
    
    st.markdown("""
        <p class="justify-text"><strong>Indonesia:</strong></p>
        <ol class="justify-text numbered-list">
                <li>Bagaimana perbedaan dalam pola penggunaan layanan bike sharing ketika dihadapkan pada empat kondisi cuaca yang berbeda, dan sejauh mana faktor cuaca memengaruhi tingkat penggunaannya?</li>
            </ol>  
        <ul class="justify-text numbered-list">
                <li>Kondisi cuaca ternyata memiliki pengaruh signifikan terhadap jumlah pengguna Bike Sharing. Saat cuaca cerah, layanan ini digunakan oleh lebih banyak orang dibandingkan dengan kondisi cuaca lainnya. Sebaliknya, ketika terjadi hujan deras, jumlah pengguna menurun drastis, menjadikannya kondisi cuaca dengan tingkat penggunaan terendah.</li>
            </ul>    
        """, unsafe_allow_html=True)

        # Garis pembatas
    st.markdown("##### ____________________________________________________________________")

        # Konten English
    st.markdown("""
            <p class="justify-text"><strong>English:</strong></p>
            <ol class="justify-text numbered-list">
                <li>How do bike-sharing usage patterns vary across four different weather conditions, and to what extent does weather influence the overall usage rate?</li>
            </ol>
        <ul class="justify-text numbered-list">
                <li>Weather conditions have a significant impact on the number of Bike Sharing users. On clear days, the service experiences a surge in usage, attracting more users compared to other weather conditions. Conversely, during heavy rainfall, the number of users drops drastically, making it the weather condition with the lowest usage rate. </li>
            </ul> 
        """, unsafe_allow_html=True)

            # Garis pembatas
    st.markdown("##### ____________________________________________________________________")
    
    # Weather Bar Chart
    fig, ax = plt.subplots(figsize=(10, 5))

    sns.set_style('whitegrid')
    sns.despine(fig)

    custom_palette = ["#800020", "#A52A2A", "#F5F5DC", "#D2B48C"]

    sns.barplot(data=weat_hour_df, x='weather', y='total', hue='weather', palette=custom_palette, edgecolor="black", legend=False)

    plt.title("Perbandingan Penggunaan Bike Sharing Pada 4 Tipe Cuaca yang Berbeda", fontsize=14, fontweight='bold', color="#800020")
    plt.xlabel(None)
    plt.ylabel(None)

    st.pyplot(fig)


st.markdown(
    "<p style='text-align: center; color: white;'>© 2025 Jihan Kusumawardhani. All Rights Reserved.</p>", 
    unsafe_allow_html=True
)
