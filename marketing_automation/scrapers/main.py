from scraper import RedditScraper
from data_processor import DataProcessor
from reporter import Reporter

def run_marketing_automation(subreddit_name):

    print(f"Starting Marketing Automation Pipeline for r/{subreddit_name}...\n")

    # Step 1: Scrape data from Reddit marketing subreddit - Extract
    scraper = RedditScraper(subreddit_name)
    raw_data = scraper.fetch_page()

    if not raw_data:
        print("No data scraped. Exiting pipeline.")
        return
    
    raw_posts = scraper.parse_data(raw_data)
    print(f"Scraped {len(raw_posts)} posts from r/{subreddit_name}.\n")
    

    # Step 2: Process the scraped data - Transform
    print("Processing and cleaning data...\n")
    processor = DataProcessor(raw_data)
    processor.clean_data()
    processed_df = processor.save_processed_data()

    # Step 3: Generate reports based on processed data - Load
    print("Generating visuals...\n")
    reporter = Reporter(processed_df)
    reporter.plot_top_posts()
    reporter.print_summary_stats()

    print('--- Automation Completed! Check the data and reports folders for results. --- ')

if __name__ == "__main__":

    target_subreddit = "marketing"
    run_marketing_automation(target_subreddit)