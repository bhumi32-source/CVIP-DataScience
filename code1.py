import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#import geopandas as gpd

# Load the terrorism dataset into a Pandas DataFrame
data = pd.read_csv("D:\coderscave\globalterrorismdb_0718dist.csv.zip", encoding='ISO-8859-1')

# Check for missing values in each column
missing_values = data.isnull().sum()

# Get the columns with missing values
blank_columns = missing_values[missing_values == len(data)].index.tolist()
# Drop the blank columns
data_cleaned = data.drop(blank_columns, axis=1)

# Initial Data Exploration
print(data.shape)  # Dimensions of the dataset
print(data.head())  # First few records
print(data.info())  # Data types and missing values

# Data Cleaning

# Statistical Summary
print(data.describe())  # Summary statistics

# Feature Engineering
# Extract year, month, and day from the date columns

plt.figure(figsize=(12, 6))
sns.countplot(data=data, x='iyear')
plt.xlabel('Year')
plt.ylabel('Number of Attacks')
plt.title('Number of Terrorist Attacks per Year')
plt.xticks(rotation=45, ha='right')
plt.tight_layout() 
plt.show()

# Bar plot: Number of attacks by country
plt.figure(figsize=(16, 6))
country_counts = data['country_txt'].value_counts().head(15)  # Limit to top 15 countries
sns.barplot(x=country_counts.index, y=country_counts.values)
plt.xlabel('Country')
plt.ylabel('Number of Attacks')
plt.title('Number of Terrorist Attacks by Country (Top 15)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Bar plot: Number of attacks by city (top 10 cities)
plt.figure(figsize=(12, 6))
city_counts = data['city'].value_counts().head(10)  # Limit to top 10 cities
sns.barplot(x=city_counts.index, y=city_counts.values)
plt.xlabel('City')
plt.ylabel('Number of Attacks')
plt.title('Number of Terrorist Attacks by City (Top 10)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Pie chart: Percentage of attacks by attack type
plt.figure(figsize=(8, 8))
attack_type_counts = data['attacktype1_txt'].value_counts()
plt.pie(attack_type_counts, labels=attack_type_counts.index, autopct='%1.1f%%')
plt.title('Percentage of Terrorist Attacks by Attack Type')
plt.tight_layout()
plt.show()
# Heatmap: Correlation matrix
corr_matrix = data[['iyear', 'country_txt', 'city', 'attacktype1_txt']].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

# Violin plot: Distribution of the number of attacks by attack type
plt.figure(figsize=(10, 6))
sns.violinplot(data=data, x='attacktype1_txt', y='iyear')
plt.xlabel('Attack Type')
plt.ylabel('Year')
plt.title('Distribution of Number of Attacks by Attack Type')
plt.xticks(rotation=45)
plt.show()
'''
# Geographic plot: Terrorist attacks worldwide
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
gdf = gpd.GeoDataFrame(data, geometry=gpd.points_from_xy(data['longitude'], data['latitude']))
fig, ax = plt.subplots(figsize=(12, 8))
world.boundary.plot(ax=ax, linewidth=0.8, color='black')
gdf.plot(ax=ax, markersize=10, color='red', alpha=0.5)
plt.title('Terrorist Attacks Worldwide')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()
'''