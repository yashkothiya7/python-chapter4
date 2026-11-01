# Create a dataframe from .csv file 

import pandas as pd
data = {
    "ID": [1, 2, 3],
    "Name": ["Aakash", "Sujal", "Milan"],
    "Marks": [85, 90, 78]
}

df = pd.DataFrame(data)

df.to_csv("Record.csv", index=False)

print("Record.csv created successfully!")

df2 = pd.read_csv("Record.csv")
print(df2)
