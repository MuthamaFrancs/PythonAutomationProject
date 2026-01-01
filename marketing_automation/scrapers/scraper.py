import requests
from bs4 import BeautifulSoup
import pandas as pd

class RedditScraper:
    def __init__(self, subreddit):
        self.subreddit = subreddit
        self.url = f"https://old.reddit.com/r/{subreddit}/"
        # We use 'old.reddit.com' because the HTML structure is more stable for scraping
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }

    def fetch_page(self):
        """Fetches the HTML content of the subreddit."""
        try:
            response = requests.get(self.url, headers=self.headers)
            response.raise_for_status() # Raise error for bad status codes (404, 500)
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data from Reddit: {e}")
            return None

    def parse_data(self, html):
        """Extracts titles and scores from HTML."""
        if not html:
            return []

        soup = BeautifulSoup(html, 'html.parser')
        posts_data = []

        # Find all post containers (on old.reddit, these are divs with class 'thing')
        posts = soup.find_all('div', class_='thing')
 
        for post in posts:
            title = post.find('a', class_='title').text
            # Scores are stored in a div with class 'score likes'
            score = post.find('div', class_='score likes').get('title', '0')
            
            posts_data.append({
                'title': title,
                'upvotes': int(score) if score.isdigit() else 0,
                'subreddit': self.subreddit
            })

        return posts_data