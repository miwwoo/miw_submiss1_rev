import os
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Dapatkan path ke script dan folder di sekitarnya
script_dir = os.path.dirname(os.path.realpath(__file__))

# Path ke file CSV di dalam folder 'dashboard'
csv_file_path = os.path.join(script_dir, 'main_data.csv')
df = pd.read_csv(csv_file_path)

# Menampilkan logo kereta
logo_path = os.path.join(script_dir, 'logo_kereta.png')  # Ganti 'logo_kereta.png' dengan nama file logo yang sesuai
st.image(logo_path, caption='cr Google', use_column_width=True)

# Dashboard title
st.title("Dashboard Data Visualisasi Air Quality Stasiun")

# Visualisasi: Scatterplot WSPM vs PM2.5
st.subheader('Wind Speed vs PM2.5 - Aotizhongxin')
plt.figure(figsize=(10, 6))
sns.scatterplot(x='WSPM', y='PM2.5', data=df)  # Ganti df dengan dataframe yang sesuai
plt.title('Wind Speed vs PM2.5 - Aotizhongxin')
plt.xlabel('Wind Speed (m/s)')
plt.ylabel('PM2.5 Concentration')
st.pyplot(plt)  # Menampilkan grafik di Streamlit
plt.clf()  # Clear the figure untuk plot selanjutnya

# Visualisasi: Scatterplot PRES vs PM2.5
st.subheader('Atmospheric Pressure vs PM2.5 - Changping')
plt.figure(figsize=(10, 6))
sns.scatterplot(x='PRES', y='PM2.5', data=df)  # Ganti df dengan dataframe yang sesuai
plt.title('Atmospheric Pressure vs PM2.5 - Changping')
plt.xlabel('Atmospheric Pressure (hPa)')
plt.ylabel('PM2.5 Concentration')
st.pyplot(plt)  # Menampilkan grafik di Streamlit
plt.clf()  # Clear the figure untuk plot selanjutnya

# Visualisasi: Scatterplot RAIN vs PM2.5
st.subheader('Rainfall vs PM2.5 - Changping')
plt.figure(figsize=(10, 6))
sns.scatterplot(x='RAIN', y='PM2.5', data=df)  # Ganti df dengan dataframe yang sesuai
plt.title('Rainfall vs PM2.5 - Changping')
plt.xlabel('Rainfall (mm)')
plt.ylabel('PM2.5 Concentration')
st.pyplot(plt)  # Menampilkan grafik di Streamlit
