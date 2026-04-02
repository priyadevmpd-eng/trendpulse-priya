import pandas as pd
import matplotlib.pyplot as plt
#read csv
df = pd.read_csv("cleaned_data.csv")
#score graph
df["score"].plot(kind="bar")
plt.title("post scores")
plt.xlabel("posts")
plt.ylabel("score")
plt.show()