import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#question 1
#a
# Load the data
data = pd.read_csv('clubmed_HW2.csv')
#group the data by age and calculate the number of people in each age group
#plot the data in a histogram
plt.hist(data.age , bins =20)
plt.xlabel('Age')
plt.ylabel('Number of people')
plt.title('Number of people in each age group')
plt.show()
#b
#you can see that most of the people are in the age group 18-60 and there are very few people in the age group 95-99