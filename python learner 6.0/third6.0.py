import pandas as pd

df = pd.read_csv("python learner 6.0/box_office_dataset.csv")

# Clean year column properly
df["year"] = pd.to_numeric(df["year"], errors="coerce")

# Remove invalid year rows
df = df.dropna(subset=["year"])

# Convert to int
df["year"] = df["year"].astype(int)

# NOW filter
df = df[df["year"] >= 2000]

print(df)