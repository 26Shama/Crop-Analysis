import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV file
data = pd.read_csv(r'C:\Users\pssha\OneDrive\Desktop\crop\crop_analysis.csv')

# Extract relevant columns (crop names and their corresponding analysis values)
crop_names = data['Crop']
analysis_values = data['Analysis']

# Plotting a pie chart
plt.figure(figsize=(8, 8))
plt.pie(analysis_values, labels=crop_names, autopct='%1.1f%%', startangle=140)
plt.title('Topic Analysis of Different Crops Growing in India')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
plt.show()

# Find the crop with the minimum analysis value
min_crop_index = analysis_values.idxmin()
min_crop_name = crop_names[min_crop_index]

# Generate message suggesting to grow the crop with the minimum analysis value next year
message = f"It is suggested to grow {min_crop_name} more next year as it had the lowest analysis value in this year."

print(message)