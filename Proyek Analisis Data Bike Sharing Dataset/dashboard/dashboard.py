import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style='dark')
plt.style.use('dark_background')

# Load dataset
file_path = "main_data.csv"
df = pd.read_csv(file_path)

df['datetime'] = pd.to_datetime(df['datetime'])

def create_casual_register_df(df):
    casual_year_df = df.groupby("year")["casual"].sum().reset_index()
    reg_year_df = df.groupby("year")["registered"].sum().reset_index()
    casual_register_df = casual_year_df.merge(reg_year_df, on="year")
    return casual_register_df

def create_monthly_df(df):
    return df.groupby(["month", "year"]).agg({"total_count": "sum"}).reset_index()

def create_hourly_df(df):
    return df.groupby(["hour", "year"]).agg({"total_count": "sum"}).reset_index()

def create_byseason_df(df):
    return df.groupby(["season", "year"]).agg({"total_count": "sum"}).reset_index()

def create_byweather_df(df):
    return df.groupby(["weather_condition", "year"]).agg({"total_count": "sum"}).reset_index()

st.title('Bike Sharing Dashboard')
st.sidebar.header("Filter Data")
start_date, end_date = st.sidebar.date_input("Select Date Range:", [df['datetime'].min(), df['datetime'].max()])

filtered_df = df[(df['datetime'] >= str(start_date)) & (df['datetime'] <= str(end_date))]

st.subheader('Total Bike Rentals Over Time')
plt.figure(figsize=(10, 4))
plt.plot(filtered_df['datetime'], filtered_df['total_count'], label='Total Rentals', color='blue')
plt.xlabel("Time")
plt.ylabel("Rentals")
plt.legend()
st.pyplot(plt)

st.subheader("Casual vs Registered Users")
casual_register_df = create_casual_register_df(filtered_df)
plt.figure(figsize=(6, 4))
plt.bar(casual_register_df["year"], casual_register_df["casual"], label="Casual", color="b")
plt.bar(casual_register_df["year"], casual_register_df["registered"], bottom=casual_register_df["casual"], label="Registered", color="g")
plt.xlabel("Year")
plt.ylabel("Total Users")
plt.legend()
st.pyplot(plt)

st.subheader("Rentals by Month")
monthly_df = create_monthly_df(filtered_df)
sns.lineplot(data=monthly_df, x="month", y="total_count", hue="year", marker="o")
plt.xlabel("Month")
plt.ylabel("Total Rentals")
st.pyplot(plt)

st.subheader("Rentals by Hour")
hourly_df = create_hourly_df(filtered_df)
sns.lineplot(data=hourly_df, x="hour", y="total_count", hue="year", marker="o")
plt.xlabel("Hour")
plt.ylabel("Total Rentals")
st.pyplot(plt)

st.subheader("Rentals by Season")
season_df = create_byseason_df(filtered_df)
sns.barplot(data=season_df, x="season", y="total_count", hue="year")
plt.xlabel("Season")
plt.ylabel("Total Rentals")
st.pyplot(plt)

st.subheader("Rentals by Weather Condition")
weather_df = create_byweather_df(filtered_df)
sns.barplot(data=weather_df, x="weather_condition", y="total_count", hue="year")
plt.xlabel("Weather Condition")
plt.ylabel("Total Rentals")
st.pyplot(plt)
