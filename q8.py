import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
#q8
#a
data = pd.read_csv('clubmed_HW2.csv')
# Calculate the IQR
Q1 = data['age'].quantile(0.25)
Q3 = data['age'].quantile(0.75)
IQR = Q3 - Q1

# Define the upper and lower bounds for outliers
upper_bound = Q3 + 1.5 * IQR
lower_bound = Q1 - 1.5 * IQR

# Create the box plot
sns.boxplot(x='ranking', y='age', data=data)

# Add horizontal lines for the upper and lower bounds
plt.axhline(upper_bound, color='r', linestyle='dashed', linewidth=2)
plt.axhline(lower_bound, color='r', linestyle='dashed', linewidth=2)

plt.title('Box plot of Age by Ranking')
plt.show()