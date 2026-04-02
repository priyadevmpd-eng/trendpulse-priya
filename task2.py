import json
import pandas as pd
#Read JSON File
with open("./data.json") as file:
    data = json.load(file)
 # This contains the Reddit data
    posts = data["data"]["children"]   
#Create empty list
post_list = []
#Using a loop to extract data
for post in posts :
    info = post["data"]
    title = info["title"]
    score = info["score"]
    author =info["author"]
    post_list.append([title,score,author])
    #creating a DataFrame 
df = pd.DataFrame(post_list,columns=["Title","score","Author"])
    # saving the CSV file
df.to_csv("cleaned_data.csv",index=False)
print("CSV file created")
