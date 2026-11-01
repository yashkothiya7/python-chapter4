#Create a DataFrame df = pd.DataFrame ({'A': [1, None, 3], 'B': [None, 4, 5]}).Fill missing values in column 'A' & 'B' with 0.
import pandas as pd

df = pd.DataFrame({
    'A': [1, None, 3],
    'B': [None, 4, 5]
})

print("----Original DataFrame:----")
print(df)

df_filled = df.fillna(0)

print("\n---DataFrame after filling missing values:---")
print(df_filled)
