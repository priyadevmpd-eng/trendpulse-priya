import pandas as pd
import matplotlib.pyplot as plt
import os

# Load data
df = pd.read_csv("data/trends_analysed.csv")

# Create outputs folder
os.makedirs("outputs", exist_ok=True)

# ------------------------------------------
# Chart 1: Top 10 Stories by Score
# ------------------------------------------
top10 = df.sort_values(by="score", ascending=False).head(10)

plt.figure()
plt.barh(top10["title"], top10["score"])
plt.xlabel("Score")
plt.ylabel("Title")
plt.title("Top 10 Stories by Score")
plt.tight_layout()

plt.savefig("outputs/chart1_top_stories.png")
plt.close()

# ------------------------------------------
# Chart 2: Stories per Category
# ------------------------------------------
category_count = df["category"].value_counts()

plt.figure()
category_count.plot(kind="bar")
plt.xlabel("Category")
plt.ylabel("Count")
plt.title("Stories per Category")
plt.tight_layout()

plt.savefig("outputs/chart2_categories.png")
plt.close()

# ------------------------------------------
# Chart 3: Score vs Comments
# ------------------------------------------
plt.figure()

# Assuming 'is_popular' column exists from previous analysis
popular = df[df["is_popular"] == True]
not_popular = df[df["is_popular"] == False]

plt.scatter(popular["score"], popular["num_comments"], label="Popular")
plt.scatter(not_popular["score"], not_popular["num_comments"], label="Not Popular")

plt.xlabel("Score")
plt.ylabel("Comments")
plt.title("Score vs Comments")
plt.legend()
plt.tight_layout()

plt.savefig("outputs/chart3_scatter.png")
plt.close()

# ------------------------------------------
# Bonus: Dashboard
# ------------------------------------------
fig, axs = plt.subplots(1, 3, figsize=(15, 5))

# Chart 1 in Dashboard
axs[0].barh(top10["title"], top10["score"])
axs[0].set_title("Top Stories")

# Chart 2 in Dashboard
category_count.plot(kind="bar", ax=axs[1])
axs[1].set_title("Categories")

# Chart 3 in Dashboard
axs[2].scatter(df["score"], df["num_comments"])
axs[2].set_title("Score vs Comments")

plt.tight_layout()
plt.savefig("outputs/dashboard.png")
plt.close()

print("All charts saved in outputs folder ✅")