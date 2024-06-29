import requests
import json
query = input("What type of news are you intreested in?")
url = f"https://newsapi.org/v2/everything?q={query}&from=2024-05-29&sortBy=publishedAt&apiKey=fdc575714ea648a5835f911e00dfa05f"
r = requests.get(url)
news = json.loads(r.text)
# print(news, type(news))
for article in news["articles"]:
    print(article["title"])
    print(article["description"])