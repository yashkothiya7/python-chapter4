import matplotlib.pyplot as plt

employee_ids = ['E101', 'E102', 'E103', 'E104', 'E105']

dept1 = [25000, 30000, 28000, 35000, 43000]
dept2 = [27000, 32000, 26000, 34000, 40000]

x = range(len(employee_ids))

plt.bar(x, dept1, width=0.4, label="Department 1")
plt.bar([i + 0.4 for i in x], dept2, width=0.4, label="Department 2")

plt.xlabel("Employee ID")
plt.ylabel("Salary (in INR)")
plt.title("Employee Salaries in Two Departments")

plt.xticks([i + 0.2 for i in x], employee_ids)

plt.legend()
plt.show()