import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
url='https://raw.githubusercontent.com/Padre-Media/dataset/main/Ames.csv'
#Load the dataset
Ames =pd.read_csv(url)
high_value_houses = Ames.query('SalePrice > 600000')
print(high_value_houses)
specific_houses = Ames.query('BedroomAbvGr > 3 & SalePrice < 300000')
#visualize the advanced query results
plt.figure(figsize=(10,7))
sns.scatterplot(x='GrLivArea',y='SalePrice',hue='BedroomAbvGr',data=specific_houses, palette='viridis')
plt.title('Sales Price vs. Ground Living Area')
plt.xlabel('Ground Living Area (sqft)')
plt.ylabel('Sales Price ($)')
plt.legend(title='Bedrooms above the ground')
plt.show()



grouped_data = specific_houses.groupby('Neighborhood').agg({'SalePrice':['mean','count']})
grouped_data.columns = ['Average Sales Price','House Count']
grouped_data['Average Sales Price']= grouped_data['Average Sales Price'].round(2)
print(grouped_data)
grouped_data_reset = grouped_data.reset_index().sort_values(by='Average Sales Price')
sns.set_theme(style="whitegrid")
#create the bar plot
plt.figure(figsize=(12,8))
barplot=sns.barplot(
    x='Neighborhood',
    y='Average Sales Price',
    data=grouped_data_reset,
    palette="coolwarm",
    hue='Neighborhood',
    legend=False,errorbar=None  # Removes the confidence interval bars
)
#rotate the x-axis label for btter readability
plt.xticks(rotation=50)
#annotate each bar with the house count using enumarate to access the index for position
for index,value in enumerate(grouped_data_reset['Average Sales Price']):
    house_count = grouped_data_reset.loc[index, 'House Count']
    plt.text(index,value,f'{house_count}',ha='center',va='bottom')
plt.title('Average Sales Price by Neighborhood', fontsize=18)
plt.xlabel('Neighborhood')
plt.ylabel('Average Sales Price (ksh)')
plt.tight_layout() #adjust the layout
plt.show()
