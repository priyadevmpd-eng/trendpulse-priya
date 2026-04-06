import pandas as pd
import json

# Load JSON file
file_path = "data/trends_20240115.json"

with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# Extract posts
posts = data["data"]["children"]

records = []
for post in posts:
    p = post["data"]
    records.append({
        "post_id": p.get("title"),
        "title": p.get("title"),
        "score": p.get("score"),
        "num_comments": 0,
        "category": "general"
    })

df = pd.DataFrame(records)

print(f"Loaded {len(df)} stories from {file_path}")

# Remove duplicates
df = df.drop_duplicates(subset="post_id")
print(f"After removing duplicates: {len(df)}")

# Remove missing values
df = df.dropna(subset=["post_id", "title", "score"])
print(f"After removing nulls: {len(df)}")

# Convert data types
df["score"] = df["score"].astype(int)
df["num_comments"] = df["num_comments"].astype(int)

# Remove low quality posts
df = df[df["score"] >= 5]
print(f"After removing low scores: {len(df)}")

# Remove extra spaces
df["title"] = df["title"].str.strip()

# Save CSV
output_path = "data/trends_clean.csv"
df.to_csv(output_path, index=False)

print(f"Saved {len(df)} rows to {output_path}")

# Category summary
print("\nStories per category:")
print(df["category"].value_counts())