import pandas as pd
import numpy as np

# Load data
df = pd.read_csv("data/trends_clean.csv")

print("Loaded data:", df.shape)

# First 5 rows
print("\nFirst 5 rows:")
print(df.head())

# Average
avg_score = df["score"].mean()
avg_comments = df["num_comments"].mean()

print("\nAverage score:", int(avg_score))
print("Average comments:", int(avg_comments))

# NumPy analysis
scores = df["score"].values

print("\n--- NumPy Stats ---")
print("Mean score:", int(np.mean(scores)))
print("Median score:", int(np.median(scores)))
print("Std deviation:", int(np.std(scores)))
print("Max score:", int(np.max(scores)))
print("Min score:", int(np.min(scores)))

# Most stories category
top_category = df["category"].value_counts().idxmax()
count = df["category"].value_counts().max()

print(f"\nMost stories in: {top_category}")