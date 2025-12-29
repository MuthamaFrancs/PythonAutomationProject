
import os # portability of code when sharing
from datetime import datetime

BASE_URL = "https://old.reddit.com/r/marketing"

#headers
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

selectors = {
    'post_container': 'div.thing',
    'title': 'a.title',
    'upvotes': 'div.score.unvoted',
    'time': 'time'
}


base_dir = os.path.dirname(os.path.abspath(__file__)) # get current file directory
data_dir = os.path.join(base_dir, 'data',) # data directory
raw_data_dir = os.path.join(data_dir, 'raw') # raw data directory
processed_data_dir = os.path.join(data_dir, 'processed') # processed data directory

# Ensure data directories exist
os.makedirs(raw_data_dir, exist_ok=True)
os.makedirs(processed_data_dir, exist_ok=True)

timestamp_format = datetime.now().strftime("%Y%m%d_%H%M%S")
raw_filename = f"reddit_marketing_raw_{timestamp_format}.csv"
