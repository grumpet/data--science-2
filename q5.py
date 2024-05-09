import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = pd.read_csv('clubmed_HW2.csv')
cross_tab_gender_club_member = pd.crosstab(index=data['gender'], columns=data['club_member'],normalize='index')
cross_tab_club_member_gender = pd.crosstab(index=data['club_member'], columns=data['gender'],normalize='index')


fig, axs = plt.subplots(2)
cross_tab_gender_club_member.plot(kind='bar', stacked=True, ax=axs[0])
axs[0].set_xlabel('gender')
axs[0].set_ylabel('club_member')
axs[0].set_title('gender by club_member')

cross_tab_club_member_gender.plot(kind='bar', stacked=True, ax=axs[1])
axs[1].set_xlabel('club_member')
axs[1].set_ylabel('gender')
axs[1].set_title('club_member by gender')
plt.tight_layout()
plt.show()

#club members are more has more connection to gender than status