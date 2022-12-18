import pandas as pd

df = pd.read_csv("allStars.csv")

print(df.shape)

del df["Luminosity"]
del df["Star Name"]
del df["Distance (ly)"]
del df["Mass (MJ)"]
del df["Radius (RJ)"]

print(df.shape)
print(list(df))

df.to_csv("clean_data.csv")