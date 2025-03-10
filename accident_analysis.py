import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from folium.plugins import HeatMap
from datetime import datetime

# Load the dataset directly from URL
dataset_url = "Us_Accidents.csv"
df = pd.read_csv(dataset_url)

# Convert Start_Time to datetime
df['Start_Time'] = pd.to_datetime(df['Start_Time'], errors='coerce')

# Handle missing values
df.fillna(method='ffill', inplace=True)

# Create subplots for multiple visualizations
fig, axes = plt.subplots(2, 2, figsize=(15, 12))

# Accidents by State
state_counts = df['State'].value_counts()[:10]
sns.barplot(x=state_counts.index, y=state_counts.values, ax=axes[0, 0])
axes[0, 0].set_title('Top 10 States with Most Accidents')
axes[0, 0].set_xlabel('State')
axes[0, 0].set_ylabel('Number of Accidents')

# Severity Analysis
severity_counts = df['Severity'].value_counts()
sns.barplot(x=severity_counts.index, y=severity_counts.values, ax=axes[0, 1])
axes[0, 1].set_title('Distribution of Accident Severity')
axes[0, 1].set_xlabel('Severity')
axes[0, 1].set_ylabel('Number of Accidents')

# Accidents by Hour
if 'Hour' not in df.columns:
    df['Hour'] = df['Start_Time'].dt.hour
sns.countplot(x=df['Hour'], ax=axes[1, 0])
axes[1, 0].set_title('Accidents by Hour of Day')
axes[1, 0].set_xlabel('Hour')
axes[1, 0].set_ylabel('Number of Accidents')

# Weather Condition Impact
if 'Weather_Condition' in df.columns:
    weather_counts = df['Weather_Condition'].value_counts()[:10]
    sns.barplot(y=weather_counts.index, x=weather_counts.values, ax=axes[1, 1])
    axes[1, 1].set_title('Top 10 Weather Conditions Leading to Accidents')
    axes[1, 1].set_xlabel('Number of Accidents')
    axes[1, 1].set_ylabel('Weather Condition')

# Save the figure
plt.tight_layout()
plt.savefig("accident_analysis.png")
plt.show()

# Hotspot Mapping (Folium)
if 'Start_Lat' in df.columns and 'Start_Lng' in df.columns:
    sample_df = df.sample(n=5000, random_state=42)
    m = folium.Map(location=[sample_df['Start_Lat'].mean(), sample_df['Start_Lng'].mean()], zoom_start=5)
    heat_data = [[row['Start_Lat'], row['Start_Lng']] for _, row in sample_df.iterrows() if not pd.isnull(row['Start_Lat']) and not pd.isnull(row['Start_Lng'])]
    HeatMap(heat_data).add_to(m)
    m.save("hotspot_map.html")
