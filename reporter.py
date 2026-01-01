import matplotlib.pyplot as plt
import seaborn as sns
import os
import pandas as pd

class Reporter:
    def __init__(self, processed_data):
        self.df = processed_data
        os.makedirs('reports', exist_ok=True)  # Ensure reports directory exists

    def plot_top_posts(self):
        # Plot top 10 posts by upvotes
        top_posts = self.df.nlargest(10, 'upvotes')
        plt.figure(figsize=(12, 6))

        #barchart
        plt.barh(top_posts['title'].str[:50] + '...', top_posts['upvotes'], color='skyblue')
        plt.xlabel('Upvotes')
        plt.title('Top 10 Reddit Marketing Posts by Upvotes')
        plt.tight_layout()
        report_path = 'reports/top_10_reddit_marketing_posts.png'
        plt.savefig(report_path)
        plt.close()
        print(f"Report saved to {report_path}")
    
    def print_summary_stats(self):
        print("\n ------- SUMMARY STATISTICS --------- \n")
        print(f"\t Total Posts Scraped: {len(self.df)}")
        print(f"\t Average Upvotes: {self.df['upvotes'].mean():.2f}")
        print(f"\t Highest Upvotes: {self.df['upvotes'].max()}")
        print(f"\t Lowest Upvotes: {self.df['upvotes'].min()}\n")
        print("--------------------------------------- \n")

def generate_chart(dataframe):
    reporter = Reporter(dataframe)
    reporter.plot_top_posts()  
    reporter.print_summary_stats()
    
