import requests
url = "https://www.reddit.com/r/news/hot.json"
headers = {
    "User-Agent": "python:trendpulse:v1.0 (by /u/testuser)"
}
response = requests.get(url,headers=headers)
print(response.status_code)