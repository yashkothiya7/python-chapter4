# Write a program to create a line graph to show the profits of a company in various years 

import matplotlib.pyplot as plt

years=range(2018,2024)
profits = [50, 65, 40, 80, 90, 120] 

plt.plot(years, profits, marker="o", color="green", linestyle="-", 
         linewidth=1, markersize=6, label="Profit")

plt.xlabel("Year")
plt.ylabel("Profit (in lakhs)")
plt.title("Company Profits Over the Years")
plt.grid(True)
plt.legend()  # show profit label at left upper corner

plt.show()
