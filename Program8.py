# Create a DataFrame with columns ['Name', 'Age', 'Score']. Sort the DataFrame based on the 'Score' column in descending order. 

import pandas as pd

data = {
    
    "Name" : ["Aakash","Rutvi","Nikita","Sujal","Himanshu"],
    "Age" : [20,19,26,21,23],
    "Score" : [95,99,91.5,55,75]
}

df = pd.DataFrame(data)
print("-----Original DataFrame-----")
print(df)

sorted_df = df.sort_values(by="Score", ascending=False)

print("\n----Sorted DataFrame :---")
print(sorted_df)
