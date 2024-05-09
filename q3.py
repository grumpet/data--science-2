import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = pd.read_csv('clubmed_HW2.csv')

cross_tab_gender_status = pd.crosstab(index=data['status'], columns=data['gender'],normalize='index')
cross_tab_status_gender = pd.crosstab(index=data['gender'], columns=data['status'],normalize='index')

fig, axs = plt.subplots(2)

cross_tab_gender_status.plot(kind='bar', stacked=True, ax=axs[0])
axs[0].set_xlabel('Status')
axs[0].set_ylabel('Gender')
axs[0].set_title('Status by Gender')

cross_tab_status_gender.plot(kind='bar', stacked=True, ax=axs[1])
axs[1].set_xlabel('Gender')
axs[1].set_ylabel('Status')
axs[1].set_title('Gender by Status')

plt.tight_layout()
plt.show()
#d males are more likely to be in a couple status in family status and single status the number of males and females are equal
#e most comon status among females is couple
#f the percentage of unmarried women is 78%
#g the percentage of male people from the single status is 27%
