#Create two DataFrames & Merge the two DataFrames(using merge()) based on the 'ID' column. 
# df1 = pd.DataFrame({'ID': [1, 2], 'Name': ['Krishna ', 'Arjun']}) df2 = pd.DataFrame({'ID': [1, 2], 'Age': [25, 30]}) 

import pandas as pd

df1 = pd.DataFrame({
    'ID': [1, 2], 
    'Name': ['Krishna','Arjun']
})

print("-----First DataFrame-----")
print(df1)

df2 = pd.DataFrame({
    'ID': [1, 2], 
    'Age': [25, 30]
})
print("\n-----Second DataFrame-----")
print(df2)

print("\n --- Merge DataFrame 1 & 2 based on I'd ---")
merge_df = pd.merge(df1, df2, on='ID')
print(merge_df)




""" 
also you can used --> [how] keyword in last of merge 
how = 'inner'
how = 'outer'
how = 'left'
how = 'right'

"""