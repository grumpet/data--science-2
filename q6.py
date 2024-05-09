import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = pd.read_csv('clubmed_HW2.csv')

sns.scatterplot(x='age', y='minibar', data=data)

plt.xlabel('Age')
plt.ylabel('Minibar')
plt.title('Scatterplot of Age vs Minibar')
plt.show()