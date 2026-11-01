# Write a program to display a histogram showing the number of employees of specific age groups.

import matplotlib.pyplot as plt

ages = [22, 25, 27, 35, 45, 26, 28, 32, 36, 41, 52, 23, 34, 38, 29, 30]
bins = [20, 30, 40, 50, 60] 

plt.hist(ages, bins, color="skyblue", edgecolor="black")

plt.xlabel("Age Groups")
plt.ylabel("Number of Employees")
plt.title("Employee Age Distribution")
plt.show()
