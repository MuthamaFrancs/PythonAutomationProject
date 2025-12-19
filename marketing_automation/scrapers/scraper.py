# scraper that pulls titles and upvotes from reddit marketing
import requests
from bs4 import BeautifulSoup

URL = "https://www.reddit.com/r/marketing/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

#Fetch the r/marketing page and extract up to 20 posts.
def scrape_reddit_marketing():
    
    #send a GET request to the URL
    response = requests.get(URL, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    posts = []
    for post in soup.find_all("shreddit-post", limit=20):
        title = post.get("post-title")
        upvotes = post.get("post-upvotes")
        
        # Convert upvotes to int if present, otherwise use "0"
        if title:
            posts.append({
                "title": title,
                "upvotes": int(upvotes) if upvotes else "0"
            })
    
    return posts

# Handle HTTP response errors status_code check timeout
#Norma;ize upvote strings like 1.2k ro integers
#Use praw  for reliable data instead of web scraping
