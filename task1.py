import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import zipfile

# Extract and load CSV file
with zipfile.ZipFile('/mnt/data/Agricultural-Production-Statistics-key-tables-from-APS-2002-2017.zip', 'r') as z:
    z.extractall('/mnt/data')
    csv_file_path = f"/mnt/data/{z.namelist()[0]}"

df = pd.read_csv(csv_file_path)  # Load the first extracted CSV file

# Display the first few rows
print(df.head())

# Basic analysis: Calculate average of a numerical column
column_name = df.select_dtypes(include=['number']).columns[0]  # First numerical column
average_value = df[column_name].mean()
print(f"Average of '{column_name}': {average_value}")

# Visualization: Bar chart
df[column_name].head(10).plot(kind='bar', title=f'Bar Chart of {column_name}', color='skyblue')
plt.show()

# Visualization: Scatter plot
plt.scatter(df.index, df[column_name], color='orange')
plt.title(f'Scatter Plot of {column_name}')
plt.show()

# Visualization: Heatmap (if applicable)
if df.select_dtypes(include=['number']).shape[1] > 1:
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
    plt.title('Correlation Heatmap')
    plt.show()
