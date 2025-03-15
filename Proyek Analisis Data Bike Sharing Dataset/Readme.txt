==========================================
Proyek Analisis Data : Bike Sharing Dataset
==========================================

Informasi Penulis:
Nama : Baiq Putri Suartikha
Email : baiqputrisuartikha239@gmail.com
ID Dicoding : Baiqputris

=========================================
Background 
=========================================

Bike-sharing systems are a modern evolution of traditional bike rentals,
where the entire process—from membership to rental and return—is automated. 
Users can rent a bike from one location and return it elsewhere. 
With over 500 programs worldwide and more than 500,000 bicycles, 
these systems play a crucial role in traffic management,environmental sustainability, and public health.  

Beyond their practical applications, bike-sharing systems generate valuable data, 
making them an attractive subject for research. Unlike buses or subways, they record precise travel durations and locations, 
effectively functioning as a virtual sensor network for urban mobility. 
This data can help detect significant city events and trends.

=========================================
Menentukan Pertanyaan Bisnis:
1. Apakah ada perbedaan dalam peminjaman sepeda di hari kerja dan akhir pekan? 
Bagaimana hari libur memengaruhi tren peminjaman sepeda?
2. Bagaimana penggunaan sepeda berkaitan dengan waktu dalam sehari? 
Apakah ada puncak waktu tertentu di mana permintaan sepeda lebih tinggi?
=========================================

=========================================
Data Wrangling:
- Dataset yang digunakan berasal dari Bike Sharing Dataset.
- Data terdiri dari:
  - day.csv: Data peminjaman sepeda berdasarkan hari.
  - hour.csv: Data peminjaman sepeda berdasarkan jam.
=========================================

=========================================
Import Library dan Load Data:
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
=========================================
# Load dataset harian
days_df = pd.read_csv('day.csv')
days_df.head()

# Load dataset jam
hours_df = pd.read_csv('hour.csv')
hours_df.head()
=========================================

Analisis Data:
Setelah melakukan pembersihan dan transformasi data, 
analisis akan dilakukan untuk menjawab pertanyaan bisnis 
menggunakan visualisasi data dan perhitungan statistik.

Hasil dan Dashboard:
Hasil analisis akan disajikan dalam bentuk visualisasi 
dan dashboard interaktif menggunakan Streamlit.
