# Write a program to display a pie chart showing the percentage of employees in each department of a company.

import matplotlib.pyplot as plt

dept = ["HR","Finance","IT","Sales","Marketing"]
emp = [20, 5, 30, 10, 35]  

plt.pie(emp, labels=dept, autopct="%1.1f%%")

plt.title("Percentage of Employees in Each Department")
plt.axis("equal")
plt.show()
