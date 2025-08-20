import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV file
data = pd.read_csv(r'C:\Users\pssha\OneDrive\Desktop\crop\crop_analysis.csv')

# Extract relevant columns (crop names and their corresponding analysis values)
crop_names = data['Crop']
analysis_values = data['Analysis']
plt.figure(figsize=(8, 8))
plt.pie(analysis_values, labels=crop_names, autopct='%1.1f%%', startangle=140)
plt.title('Topic Analysis of Different Crops Growing in India')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
plt.show()
# Find the indices of the three crops with the lowest analysis values
min_crop_indices = analysis_values.nsmallest(3).index

# Get the names of the three crops
min_crop_names = crop_names[min_crop_indices]

# Generate message suggesting to grow the three crops more next year
message = f"It is suggested to grow the following three crops more next year as they had the lowest analysis values in this year: {', '.join(min_crop_names)}."

print(message)