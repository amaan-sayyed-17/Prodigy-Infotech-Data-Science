from pathlib import Path
from collections import Counter
import re
import sys
import matplotlib.pyplot as plt
import pandas as pd

DATA_URL = (
    "https://raw.githubusercontent.com/Prodigy-InfoTech/"
    "data-science-datasets/main/Task%204/twitter_training.csv"
)

BASE = Path(__file__).resolve().parent
OUTPUT = BASE / "outputs"
OUTPUT.mkdir(exist_ok=True)

input_path = Path(sys.argv[1]) if len(sys.argv) > 1 else None
source = str(input_path) if input_path else DATA_URL
columns = ["ID", "Topic", "Sentiment", "Tweet"]
df = pd.read_csv(source, header=None, names=columns)

print("Original shape:", df.shape)
print("\nMissing values:")
print(df.isna().sum())

df = df.dropna(subset=["Topic", "Sentiment", "Tweet"]).copy()
df["Topic"] = df["Topic"].astype(str).str.strip()
df["Sentiment"] = df["Sentiment"].astype(str).str.strip().str.title()
df["Tweet"] = df["Tweet"].astype(str).str.strip()
df = df[df["Tweet"].ne("")]
valid_sentiments = {"Positive", "Negative", "Neutral", "Irrelevant"}
df = df[df["Sentiment"].isin(valid_sentiments)].copy()

def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+|www\S+", " ", text)
    text = re.sub(r"@\w+", " ", text)
    text = re.sub(r"#\w+", " ", text)
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

df["Clean_Tweet"] = df["Tweet"].map(clean_text)
df["Tweet_Length"] = df["Clean_Tweet"].str.len()
df.to_csv(OUTPUT / "twitter_cleaned.csv", index=False)

sentiment_counts = df["Sentiment"].value_counts()
plt.figure(figsize=(8, 5))
plt.bar(sentiment_counts.index, sentiment_counts.values)
plt.xlabel("Sentiment")
plt.ylabel("Number of posts")
plt.title("Overall Social Media Sentiment Distribution")
plt.tight_layout()
plt.savefig(OUTPUT / "sentiment_distribution.svg", bbox_inches="tight")
plt.close()

top_topics = df["Topic"].value_counts().head(10).index
topic_sentiment = pd.crosstab(
    df.loc[df["Topic"].isin(top_topics), "Topic"],
    df.loc[df["Topic"].isin(top_topics), "Sentiment"],
).reindex(columns=["Positive", "Negative", "Neutral", "Irrelevant"], fill_value=0)
topic_sentiment.to_csv(OUTPUT / "sentiment_by_topic.csv")
topic_sentiment.plot(kind="bar", figsize=(12, 6))
plt.xlabel("Topic / Entity")
plt.ylabel("Number of posts")
plt.title("Sentiment Distribution Across Top 10 Topics")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig(OUTPUT / "sentiment_by_topic.svg", bbox_inches="tight")
plt.close()

plt.figure(figsize=(9, 6))
for sentiment in ["Positive", "Negative", "Neutral", "Irrelevant"]:
    values = df.loc[df["Sentiment"] == sentiment, "Tweet_Length"]
    if not values.empty:
        plt.hist(values, bins=30, alpha=0.45, label=sentiment)
plt.xlabel("Cleaned tweet length (characters)")
plt.ylabel("Number of posts")
plt.title("Tweet Length Distribution by Sentiment")
plt.legend()
plt.tight_layout()
plt.savefig(OUTPUT / "tweet_length_by_sentiment.svg", bbox_inches="tight")
plt.close()

stopwords = {
    "the", "and", "for", "you", "that", "with", "this", "was", "are", "have",
    "not", "but", "from", "they", "its", "what", "your", "just", "will",
    "about", "can", "all", "has", "had", "out", "get", "our", "his", "her",
    "too", "who", "how", "why", "when", "where", "been", "were", "their",
    "there", "them", "than", "then", "into", "over", "more", "one", "some",
}

def top_words(series, n=15):
    words = []
    for text in series:
        words.extend(word for word in text.split() if len(word) > 2 and word not in stopwords)
    return Counter(words).most_common(n)

word_rows = []
for sentiment in ["Positive", "Negative", "Neutral", "Irrelevant"]:
    for word, count in top_words(df.loc[df["Sentiment"] == sentiment, "Clean_Tweet"]):
        word_rows.append({"Sentiment": sentiment, "Word": word, "Count": count})
pd.DataFrame(word_rows).to_csv(OUTPUT / "top_words_by_sentiment.csv", index=False)

summary = pd.DataFrame({
    "metric": [
        "rows_after_cleaning", "unique_topics", "positive_posts", "negative_posts",
        "neutral_posts", "irrelevant_posts"
    ],
    "value": [
        len(df), df["Topic"].nunique(), int((df["Sentiment"] == "Positive").sum()),
        int((df["Sentiment"] == "Negative").sum()), int((df["Sentiment"] == "Neutral").sum()),
        int((df["Sentiment"] == "Irrelevant").sum())
    ],
})
summary.to_csv(OUTPUT / "eda_summary.csv", index=False)

print("\nTask 04 completed. Outputs saved in the outputs folder.")
