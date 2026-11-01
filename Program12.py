#Write a program to display employee id numbers on X-axis and their salaries on Y- axis in the form of bar graph

import matplotlib.pyplot as plt

employee_ids = ['E101', 'E102', 'E103', 'E104', 'E105']
salaries = [25000, 30000, 28000, 35000, 40000]

plt.bar(employee_ids, salaries)

plt.xlabel("Employee ID")
plt.ylabel("Salary(in INR)")
plt.title("Employee Salaries by I'd")

plt.show()

