
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


file_path = 'crime-data.csv'
crime_data = pd.read_csv(file_path)

print("The head of the dataset:")
print(crime_data.head())

print("Informations about the dataset:")
print(crime_data.info())

# Drop rows with missing values
crime_data_cleaned = crime_data.dropna()

print("Missing values in cleaned dataset:")
print(crime_data_cleaned.isnull().sum())

# Informations about the cleaned dataset 
print("\nInformations about the cleaned dataset:")
print(crime_data_cleaned.info())

print("Missing values in cleaned dataset:")
print(crime_data_cleaned.isnull().sum())


# Analyze crime types
crime_types = crime_data_cleaned['Primary Type'].unique()
print("\nCrime Types:")
print(crime_types)


# Analyze distribution of crime types
crime_type_counts = crime_data_cleaned['Primary Type'].value_counts()
print("\nCrime Type Distribution:")
print(crime_type_counts)


# Get the top 5 crime types by count
top_crime_types = crime_type_counts.nlargest(5)

# Print the number of occurrences for each top crime type
print("\nTop 5 Crime Types:")
for crime_type, count in top_crime_types.items():
    print(f"{crime_type}: {count}")



# Plotting the bar chart
plt.figure(figsize=(10, 6))
crime_type_counts.plot(kind='bar', color='skyblue')
plt.title('Les Tendances Criminelles')
plt.xlabel('Crime Type')
plt.ylabel('Number of Crimes')
plt.xticks(rotation=45, ha='right') 
plt.tight_layout()

# Save the plot
plt.savefig('les_tendances_criminelles_bar_chart.png')

# Plotting the pie chart
plt.figure(figsize=(10, 6))
colors = plt.cm.Paired.colors
ax = crime_type_counts.plot(kind='pie', autopct='', startangle=140, labels=None, colors=colors)

plt.title('Les Tendances Criminelles')

plt.axis('equal')

# Add a legend 
ax.legend(labels=[f'{crime_type} ({percentage:.1f}%)' for crime_type, percentage in 
zip(crime_type_counts.index, crime_type_counts / crime_type_counts.sum() * 100)],    
loc="center left", bbox_to_anchor=(1, 0.5))

# Save the plot
plt.savefig('les_tendances_criminelles_pie.png', bbox_inches='tight')


# Count of crimes in each Community Area
plt.figure(figsize=(18, 8))
sns.countplot(x='Community Area', data=crime_data_cleaned, palette='viridis')

plt.title('Nombre de Crimes par Zone (Community Area)')
plt.xlabel('Community Area')
plt.ylabel('Nombre de Crimes')
plt.xticks(rotation=90)

# Save the plot 
plt.savefig('Nombre_de_crimes_par_zone.png')

# Get the top 5 Community Areas
top_community_areas = crime_data_cleaned['Community Area'].value_counts().nlargest(5).index

# Filter the dataset for the top 5 Community Areas
top_areas_data = crime_data_cleaned[crime_data_cleaned['Community Area'].isin(top_community_areas)]

# Create a count plot of crimes in the top 5 Community Areas
plt.figure(figsize=(12, 8))
sns.countplot(x='Community Area', data=top_areas_data, palette='viridis')

plt.title('Top 5 zones à haut risque de criminalité. ')
plt.xlabel('Community Area')
plt.ylabel('Crime Count')
plt.xticks(rotation=45)
plt.savefig('top_5_zones.png')

total_community_areas = crime_data_cleaned['Community Area'].nunique()

# Print the total number of community areas
print(f"\nNumero total de Community Areas: {total_community_areas}")

# Print the number of crimes in each top community area
print("\nNumero de Crimes dans  Top 5 zones:")
for community_area, count in top_community_areas.items():
    print(f"Community Area {community_area}: {count} crimes")

# Get the top 5 Community Areas by crime count
top_community_areas = crime_data_cleaned['Community Area'].value_counts().nlargest(5)

# Print the number of crimes in each top community area
print("\nNombre de crime dans Top 5 zones:")
for community_area, count in top_community_areas.items():
    print(f"Community Area {community_area}: {count} crimes")

# Calculate the total number of community areas
total_community_areas = crime_data_cleaned['Community Area'].nunique()

# Print the total number
print(f"\nNombre total de Community Areas: {total_community_areas}")

total_crimes = crime_data_cleaned.shape[0]
percentage_by_area = (top_community_areas / total_crimes) * 100

# percentage of crimes for each top community area
print("\nPourcentage de  Crimes dans Top 5 zones:")
for community_area, percentage in percentage_by_area.items():
    print(f"Community Area {community_area}: {percentage:.2f}% des crimes totaux")


# Filter the dataset for the top 5 Community Areas
top_areas_data = crime_data_cleaned[crime_data_cleaned['Community Area'].isin(top_community_areas)]

# Community Area numbers to names
area_mapping = {
    30: 'South Lawndale',
    27: 'E. Garfield Park',
    29: 'North Lawndale',
    25: 'Austin',
    8: 'Lincoln Park'
}

# Replace Community Area numbers with names
top_areas_data['Community Area'] = top_areas_data['Community Area'].map(area_mapping)
plt.figure(figsize=(12, 8))
sns.countplot(x='Community Area', data=top_areas_data, palette='viridis')

plt.title('Top 5 zones à haut risque de criminalité')
plt.xlabel('Community Area')
plt.ylabel('Crime Count')
plt.xticks(rotation=45)
plt.savefig('top_5_zones.png')

# Create a pie chart with legend
crime_counts_by_area = top_areas_data['Community Area'].value_counts()
plt.figure(figsize=(10, 8))
colors = plt.cm.Paired.colors
explode = (0.1, 0, 0, 0, 0)
wedges, texts, autotexts = plt.pie(crime_counts_by_area, labels=None, autopct='%1.1f%%', startangle=140, colors=colors, explode=explode)

plt.title('Distribution des crimes dans les 5 zones à haut risque')
plt.legend(wedges, crime_counts_by_area.index, title='Community Areas', loc='center left', bbox_to_anchor=(1, 0.5))
plt.axis('equal')

plt.savefig('distribution_crimes_top_5_zones.png', bbox_inches='tight')
