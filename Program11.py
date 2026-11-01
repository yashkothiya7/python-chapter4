#Create a DataFrame df = pd.DataFrame({'Category': ['A', 'B', 'A', 'B'], 'Value': [10, 20, 30, 40]}).Group the data by the 'Category' 
# column and calculate the multiple aggregation functions like mean, maximum and minimum of the 'Value' for each group. 

import pandas as pd

df = pd.DataFrame({
    'Category': ['A', 'B', 'A', 'B'],
    'Value': [10, 20, 30, 40]
})

print("----Original DataFrame:----")
print(df)

grouped_data = df.groupby('Category')['Value'].agg(['mean', 'max', 'min'])

print("--- Aggregated Data ---")
print(grouped_data)