import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
#q7
#a
data = pd.read_csv('clubmed_HW2.csv')
summary = data['room_price'].describe()
q1 = summary['25%']
print('First Quartile (Q1):', q1)
q2 = summary['50%']
print('Second Quartile (Q2):', q2)
q3 = summary['75%']
print('Third Quartile (Q3):', q3)
q4 = summary['max']
print('Fourth Quartile (Q4):', q4)
std = summary['std']
print('Standard Deviation:', std)
IQR = summary['75%'] - summary['25%']
print('Interquartile Range (IQR):', IQR)
#b
mean = summary['mean']
num_rooms = data[data['room_price'] <= mean].shape[0]
print('Number of rooms with price equal to or lower than the mean:', num_rooms)
# that number is like that because of the skewness of the data
#c
plt.hist(data['room_price'], bins=20)
plt.xlabel('Room Price')
plt.ylabel('Number of Rooms')
plt.title('Number of Rooms in Each Price Group')
plt.axvline(mean, color='r', linestyle='dashed', linewidth=2, label=f'Mean: {mean:.2f}')
plt.axvline(mean - std, color='g', linestyle='dashed', linewidth=2, label=f'Standard Deviation: {std:.2f}')
plt.axvline(mean + std, color='g', linestyle='dashed', linewidth=2)
plt.show()
#d
#the room price is right skewed and high spread