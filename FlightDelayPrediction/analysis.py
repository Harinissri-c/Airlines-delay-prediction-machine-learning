import pandas as pd
import numpy as np
import json
import os

def generate_analysis():
    print("Loading data for analysis...")
    data_path = r'c:\Users\kiran\Downloads\DelayedFlights.csv\DelayedFlights.csv'
    # Use a larger subset for analysis to get better trends
    df = pd.read_csv(data_path, nrows=500000)
    
    analysis_results = {}
    
    print("Analyzing delay causes...")
    # Calculate averages for cause-related columns
    causes = ['CarrierDelay', 'WeatherDelay', 'NASDelay', 'SecurityDelay', 'LateAircraftDelay']
    # Filter only rows where there is a delay
    delayed_df = df[df['ArrDelay'] > 0]
    
    cause_means = delayed_df[causes].mean().to_dict()
    analysis_results['delay_causes'] = cause_means
    
    print("Calculating month-wise weather delays...")
    weather_by_month = df.groupby('Month')['WeatherDelay'].mean().to_dict()
    analysis_results['weather_by_month'] = weather_by_month
    
    print("Generating heatmap data (by Origin)...")
    # Top 50 airports by delay frequency
    origin_delays = df[df['ArrDelay'] > 30].groupby('Origin').size().sort_values(ascending=False).head(50)
    analysis_results['heatmap_origins'] = origin_delays.to_dict()
    
    print("Saving analysis results...")
    output_dir = r'c:\Users\kiran\Downloads\DelayedFlights.csv\FlightDelayPrediction\data'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    with open(os.path.join(output_dir, 'analysis_stats.json'), 'w') as f:
        json.dump(analysis_results, f)
    
    print("Analysis complete.")

if __name__ == '__main__':
    generate_analysis()
