#Create a Pandas Series from a list of integers 

import pandas as pd

numbers = [10, 20, 30, 40, 50]

series = pd.Series(numbers)
print("Series with default index number - ")
print(series,"\n")

# try to change index as per your choice 
series1 = pd.Series(numbers, index=["a", "b", "c", "d", "e"])
print("Series with user define index number - ")
print(series1)
