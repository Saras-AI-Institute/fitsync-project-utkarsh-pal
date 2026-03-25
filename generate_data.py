import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Define the date range
start_date = '2025-01-01'
date_range = pd.date_range(start=start_date, periods=365, freq='D')

# Generate realistic fitness data
steps = np.random.normal(loc=8500, scale=2500, size=365).clip(3000, 18000)
sleep_hours = np.random.normal(loc=7.2, scale=1.0, size=365).clip(4.5, 9.5)
heart_rate = np.random.normal(loc=68, scale=10, size=365).clip(48, 110)
calories_burned = np.random.randint(1800, 4200, size=365)
active_minutes = np.random.randint(20, 180, size=365)

# Create a DataFrame
fitness_data = pd.DataFrame({
    'Date': date_range,
    'Steps': steps,
    'Sleep_Hours': sleep_hours,
    'Heart_Rate_bpm': heart_rate,
    'Calories_Burned': calories_burned,
    'Active_Minutes': active_minutes
})

# Introduce 5% missing values randomly in each column
for column in fitness_data.columns[1:]:  # Skip 'Date' column
    fitness_data.loc[fitness_data.sample(frac=0.05).index, column] = np.nan

# Save the DataFrame to a CSV file
fitness_data.to_csv('data/health_data.csv', index=False)