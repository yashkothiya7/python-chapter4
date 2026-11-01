# 6.Create a dataframe from a dictionary

import pandas as pd
print("\n ------------Data frame form a dictionary ------------")
# Create a dictionary 
data = {
    "Name": ["Aakash", "rutvi", "Raj", "nikita"],
    "Age": [21, 22, 20, 23],
    "City": ["Ahmedabad", "Surat", "Vadodara", "Rajkot"]
}
df = pd.DataFrame(data)
print(df)


# using list of list
print("\n\n ------------Data frame form a list of list------------")
import pandas as pd

data = [
    ["Aakash", 21, "Ahmedabad"],
    ["rutvi", 22, "Surat"],
    ["Raj", 20, "Vadodara"],
    ["nikita", 23, "Rajkot"]
]
df = pd.DataFrame(data, columns=["Name", "Age", "City"])
print(df)
