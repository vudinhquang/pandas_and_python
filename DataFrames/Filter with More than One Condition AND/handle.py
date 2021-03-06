import pandas as pd

df = pd.read_csv("../employees.csv", parse_dates = ["Start Date", "Last Login Time"])

df["Senior Management"] = df["Senior Management"].astype("bool")
df["Gender"] = df["Gender"].astype("category")
print(df.head(3))
df.info()

mask1 = df["Gender"] == "Male"
mask2 = df["Team"] == "Marketing"

print(df[mask1 & mask2])