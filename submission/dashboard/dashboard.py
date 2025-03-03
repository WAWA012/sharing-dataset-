import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Set theme
sns.set_theme(style='dark')

# Load dataset
dataset_bike = pd.read_csv("submission?dashboard/main_data.csv")

# Convert 'dateday' to datetime format
dataset_bike['dateday'] = pd.to_datetime(dataset_bike['dateday'])

# Convert 'hour' to numeric format
dataset_bike['hour'] = dataset_bike['hour'].str.extract(r'(\d+)').astype(int)

# Get min and max date
min_date = dataset_bike['dateday'].min()
max_date = dataset_bike['dateday'].max()

# Sidebar - Date Range Selection
with st.sidebar:
    st.image("https://images.unsplash.com/photo-1496147433903-1e62fdb6f4be?q=80&w=1421&auto=format&fit=crop")
    start_date, end_date = st.date_input(
        "Rentang tanggal", [min_date, max_date], min_value=min_date, max_value=max_date
    )

    # Filter dataset based on date range
    df_filtered = dataset_bike[(dataset_bike['dateday'] >= pd.Timestamp(start_date)) & 
                               (dataset_bike['dateday'] <= pd.Timestamp(end_date))]

# Calculate total rentals
total_rentals = df_filtered['total'].sum()

# Display total rentals
st.header("Bike Sharing Dashboard")
st.metric("Total Penyewaan", value=total_rentals)

# Plot daily rental trends
st.subheader("Tren Penyewaan Harian")
plt.figure(figsize=(10, 5))
sns.lineplot(x='dateday', y='total', data=df_filtered, marker='o', color='#A5DD9B')
plt.xlabel("Tanggal")
plt.ylabel("Total Penyewaan")
st.pyplot(plt)

# Plot hourly rental distribution
st.subheader("Distribusi Penyewaan per Jam")
plt.figure(figsize=(10, 5))
sns.barplot(x='hour', y='total', data=df_filtered, palette='coolwarm')
plt.xlabel("Jam")
plt.ylabel("Total Penyewaan")
st.pyplot(plt)
