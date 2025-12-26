# scraper that pulls titles and upvotes from reddit marketing
import requests
from bs4 import BeautifulSoup

URL = "https://www.reddit.com/r/marketing/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

print(f"Starting Reddit marketing scraper from:{URL}")

try:
    response = requests.get(URL, headers=headers)
    response.raise_for_status()
    print(f"Status Code:{response.status_code}","Connection to Reddit marketing page successful.")
except requests.exceptions.RequestException as e:
    print(f"Error connecting to Reddit marketing page: {e}")

soup = BeautifulSoup(response.content, "html.parser")
posts = []

def scrape_reddit_marketing():
    
    for post in soup.find_all("shreddit-post",):
        #Extract title and upvotes
        #title_element = post.find("a", atrrs={'slot':'full-post-link'})
        #title = title_element.get_text(strip=True) if title_element else None
        title = post.get('post-title')

        #upvotes_element = post.find('faceplate-number')
        #upvotes = upvotes_element.get('number') if upvotes_element else 
        upvotes = post.get('score')

        posts.append({
            "title": title, 
            "upvotes": int(upvotes) if upvotes else 0
        })

    print(f"Successfully scraped  {len(posts)} posts from Reddit marketing.")
    return posts

scrape_reddit_marketing()
