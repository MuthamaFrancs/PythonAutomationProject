import pandas as pd
import os

class DataProcessor:
    def __init__(self, raw_data):
        self.df = pd.DataFrame(raw_data) # Initialize DataFrame from raw data

    def clean_data(self):

        if self.df.empty:
            print("No data to process.")
            return self.df
        
        # Remove duplicate rows
        initial_count = len(self.df)
        self.df.drop_duplicates( subset=['title'], keep='first', inplace=True)


        # Fill missing upvotes with 0
        self.df['upvotes'] = self.df['upvotes'].fillna(0)

        print(f"Cleaned data: removed {initial_count - len(self.df)} duplicate rows.")

        #Title length filter
        self.df['title_length'] = self.df['title'].apply(len)

        #Engagemnt category into High, Medium, Low based on upvotes
        #Helpful to see which posts are performing well/ Trending
        def categorize_engagement(upvotes):
            if upvotes >= 100:
                return 'High'
            elif upvotes >= 50:
                return 'Medium'
            else:
                return 'Low'
        
        self.df['engagement_level'] = self.df['upvotes'].apply(categorize_engagement)
    
    def save_processed_data(self, filename="processed_reddit_marketing_data.csv"):

        os.makedirs('data/processed', exist_ok=True )# ensure directory exists if not creates it
        path = os.path.join('data', 'processed', filename)
        self.df.to_csv(path, index=False)
        print(f"Processed data saved to {path}")
        return self.df