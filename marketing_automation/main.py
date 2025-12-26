from scrapers.scraper import scrape_reddit_marketing as scrape_marketing_posts
from scrapers.data_processor import process_posts
from scrapers.reporter import generate_chart

def main():
    posts = scrape_marketing_posts()
    df = process_posts(posts)
    generate_chart(df)

if __name__ == "__main__":
    main()
