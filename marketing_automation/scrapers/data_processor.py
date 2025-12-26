import pandas as pd

def process_posts(posts):
    df = pd.DataFrame(posts)

    df["title_length"] = df["title"].apply(len)
    df = df.sort_values(by="upvotes", ascending=False)

    df.to_csv("data/processed/marketing_trends.csv")

    return df
