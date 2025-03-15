import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
file_path = "main_data.csv"
df = pd.read_csv(file_path)

# Convert datetime column to proper format
df['datetime'] = pd.to_datetime(df['datetime'])

def main():
    st.title("Bike Sharing Dashboard")
    st.sidebar.header("Filter Data")
    
    # Sidebar filters
    selected_season = st.sidebar.multiselect("Select Season:", df['season'].unique(), default=df['season'].unique())
    selected_weather = st.sidebar.multiselect("Select Weather Condition:", df['weather_condition'].unique(), default=df['weather_condition'].unique())
    
    filtered_df = df[(df['season'].isin(selected_season)) & (df['weather_condition'].isin(selected_weather))]
    
    # Display filtered dataset summary
    st.subheader("Data Overview")
    st.write(filtered_df.describe())
    
    # Time series analysis
    st.subheader("Total Bike Rentals Over Time")
    plt.figure(figsize=(10, 4))
    plt.plot(filtered_df['datetime'], filtered_df['total_count'], label='Total Rentals', color='blue')
    plt.xlabel("Time")
    plt.ylabel("Rentals")
    plt.legend()
    st.pyplot(plt)
    
    # Correlation heatmap
    st.subheader("Correlation Heatmap")
    plt.figure(figsize=(8, 5))
    sns.heatmap(filtered_df[['temp', 'humidity', 'windspeed', 'total_count']].corr(), annot=True, cmap='coolwarm')
    st.pyplot(plt)
    
    # Rentals by season
    st.subheader("Bike Rentals by Season")
    season_counts = df.groupby('season')['total_count'].sum()
    plt.figure(figsize=(6, 4))
    season_counts.plot(kind='bar', color=['red', 'green', 'blue', 'purple'])
    plt.xlabel("Season")
    plt.ylabel("Total Rentals")
    st.pyplot(plt)

if __name__ == "__main__":
    main()