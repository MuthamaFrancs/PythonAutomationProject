# scraper that pulls titles and upvotes from reddit marketing
import requests
from bs4 import BeautifulSoup
import config


def fetch_html(url, headers):
    try:
        print(f'Fetching HTML content from: {url}...')
        response = requests.get(url, headers=config.HEADERS)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching HTML content: {e}")
        return None

soup = BeautifulSoup(fetch_html(config.BASE_URL,config.HEADERS), 'html.parser')
posts_data = []

posts = soup.select(config.selectors['post_container'])

def scrape_reddit_marketing():
    for post in soup.find_all("shreddit-post",):
        #Extract title and upvotes
        title_element = post.select_one(config.selectors['title'])
        title = title_element.text.strip() if title_element else "N/A"

        #Extract upvotes
        upvotes_element = post.select_one(["score"])
        if upvotes_element and title_element.has_attr("title"):
            upvotes = upvotes_element["title"]
        elif upvotes_element:
            upvotes = upvotes_element.text.strip()
        else:
            upvotes = "0"

        #Extract post creation time
        time_element = post.select_one(config.selectors['time'])
        created_at = time_element['datetime'] if time_element else None

        #Append extracted data to posts list
        posts.append({
            "title": title, 
            "upvotes": upvotes,
            "created_at": created_at
        })

    print(f"Successfully scraped  {len(posts)} posts from Reddit marketing.\n")
    return posts_data

scrape_reddit_marketing()
