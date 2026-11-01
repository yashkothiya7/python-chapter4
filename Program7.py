#Create a DataFrame with columns ['Name', 'City']. Access column "City" and display it
import pandas as pd

data = {
    "Name": ["Aakash", "rutvi", "nikita","himanshu"],
    "City": ["Ahmedabad", "Surat", "Rajkot","Vadodara"]
}
df = pd.DataFrame(data)

print("-----Full DataFrame:-----")
print(df)

city_column = df['City']
print("\n---City column:---")
print(city_column)
