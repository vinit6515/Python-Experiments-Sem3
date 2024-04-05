import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Create a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma'],
    'Age': [25, 30, np.nan, 22, 28],
    'Salary': [50000, 60000, 75000, np.nan, 55000],
    'City': ['New York', 'Los Angeles', 'Chicago', 'San Francisco', 'Boston']
}

df = pd.DataFrame(data)

# Display the DataFrame
print("Original DataFrame:")
print(df)

# Save DataFrame to a CSV file
df.to_csv('example_data.csv', index=False)

# Read data from CSV file
df_read = pd.read_csv('example_data.csv')

# Drop rows with any NA values
df_cleaned = df.dropna()

# Drop NA values of specific columns
df_cleaned_specific = df.dropna(subset=['Age'])

# Fill NA values with random values, mean, median
df_filled_random = df.fillna(value=np.random.randint(20, 40), inplace=False)
df_filled_mean = df.fillna(value=df.mean(), inplace=False)
df_filled_median = df.fillna(value=df.median(), inplace=False)

# Display statistical information of the DataFrame
statistics = df.describe()

# Establish a relationship between columns
relationship = df.corr()

# Plotting using matplotlib
plt.figure(figsize=(12, 6))

# Bar chart
plt.subplot(2, 2, 1)
df.plot(kind='bar', x='Name', y='Age', title='Bar Chart')

# Pie chart
plt.subplot(2, 2, 2)
df['Age'].plot(kind='pie', autopct='%1.1f%%', title='Pie Chart')

# Scatter plot
plt.subplot(2, 2, 3)
df.plot(kind='scatter', x='Age', y='Salary', title='Scatter Plot')

# Histogram
plt.subplot(2, 2, 4)
df['Salary'].plot(kind='hist', bins=5, title='Histogram')

plt.tight_layout()
plt.show()
