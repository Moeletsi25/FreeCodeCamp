import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Import data from CSV
df = pd.read_csv('epa-sea-level.csv')

# Create scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='b', label='Data Points')

# Calculate line of best fit for all data
slope, intercept, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
x_values = range(1880, 2051)
y_values = slope * x_values + intercept
plt.plot(x_values, y_values, color='r', label='Line of Best Fit (1880-2050)')

# Calculate line of best fit for data from 2000 onwards
recent_data = df[df['Year'] >= 2000]
slope_recent, intercept_recent, _, _, _ = linregress(recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])
y_values_recent = slope_recent * x_values + intercept_recent
plt.plot(x_values, y_values_recent, color='g', label='Line of Best Fit (2000-2050)')

# Set labels and title
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')
plt.axvline(x=2050, color='gray', linestyle='--', label='Prediction Year (2050)')
plt.legend()

# Save and show the plot
plt.savefig('sea_level_scatter_plot.png')
plt.show()
