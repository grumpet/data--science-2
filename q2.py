import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
#q2
data = pd.read_csv('clubmed_HW2.csv')

sns.countplot(x='club_member', data=data, palette='hsv')

plt.xlabel('True or False')
plt.ylabel('Number of people')
plt.title('How many people are club members?')
plt.show()