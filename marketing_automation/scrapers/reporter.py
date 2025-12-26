import matplotlib.pyplot as plt

def generate_chart(df):
    top_posts = df.head(10)

    plt.figure()
    plt.barh(top_posts["title"], top_posts["upvotes"])
    plt.xlabel("Upvotes")
    plt.title("Top Marketing Topics on Reddit")

    plt.tight_layout()
    plt.savefig("reports/charts/top_marketing_topics.png")
