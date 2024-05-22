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
                

