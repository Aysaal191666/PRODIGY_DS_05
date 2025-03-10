# PRODIGY_DS_05
Analysis and visualization of US traffic accident data.
# US Accident Analysis & Hotspot Mapping

This project analyzes traffic accident data to identify patterns related to road conditions, weather, and time of day. It also visualizes accident hotspots using Folium.

## Dataset
The dataset is sourced from the US Accidents dataset available at [Kaggle](https://www.kaggle.com/code/harshalbhamare/us-accident-eda).

## Features
- **Accident Distribution by State**
- **Severity Analysis**
- **Weather Condition Impact**
- **Time-based Patterns** (Hourly & Daily Trends)
- **Hotspot Mapping using Folium HeatMap**

## Installation
Clone the repository and install the required dependencies:
```sh
pip install -r requirements.txt
```

## Usage
Run the analysis script:
```sh
python us_accident_analysis.py
```
The interactive accident hotspot map will be saved as `hotspot_map.html`.

## Dependencies (`requirements.txt`)
```
pandas
numpy
matplotlib
seaborn
folium
```

## Results
- Bar plots for accident severity, state-wise distribution, and weather impact
- Time-based accident trends
- Interactive accident hotspot map

## Hotspot Map Output
After running the script, open `hotspot_map.html` to view the interactive accident heatmap.

## License
This project is for educational purposes only.
