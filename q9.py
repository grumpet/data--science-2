import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
#q9
#a) the answer is 6

data = pd.read_csv('clubmed_HW2.csv')
Q1_price = data['room_price'].quantile(0.25)
Q3_price = data['room_price'].quantile(0.75)
IQR_price = Q3_price - Q1_price

upper_bound_price = Q3_price + 1.5 * IQR_price
lower_bound_price = Q1_price - 1.5 * IQR_price

fig, axs = plt.subplots(2, 1, figsize=(10, 10))

Q1_age = data['age'].quantile(0.25)
Q3_age = data['age'].quantile(0.75)
IQR_age = Q3_age - Q1_age

upper_bound_age = Q3_age + 1.5 * IQR_age
lower_bound_age = Q1_age - 1.5 * IQR_age

sns.boxplot(x='visits5years', y='age', data=data, ax=axs[0])

axs[0].axhline(upper_bound_age, color='r', linestyle='dashed', linewidth=2)
axs[0].axhline(lower_bound_age, color='r', linestyle='dashed', linewidth=2)

axs[0].set_title('Box plot of Age by Visits in 5 Years')

sns.boxplot(x='visits5years', y='room_price', data=data, ax=axs[1])

axs[1].axhline(upper_bound_price, color='b', linestyle='dashed', linewidth=2)
axs[1].axhline(lower_bound_price, color='b', linestyle='dashed', linewidth=2)

axs[1].set_title('Box plot of Room Price by Visits in 5 Years')

#b) ????????????????????????????????????????????????
plt.tight_layout()
plt.show()