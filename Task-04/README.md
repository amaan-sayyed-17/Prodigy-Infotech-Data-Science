# Task 04 — Social Media Sentiment Analysis

## Objective

Analyze and visualize sentiment patterns in social media data to understand public opinion and attitudes toward specific topics or brands.

## Dataset

This project uses the official Prodigy InfoTech Task 04 dataset:

- File: `twitter_training.csv`
- Source: https://github.com/Prodigy-InfoTech/data-science-datasets/tree/main/Task%204

The CSV is loaded without a header and interpreted as:

1. `ID` — unique identifier
2. `Topic` — topic/entity mentioned in the post
3. `Sentiment` — Positive, Negative, Neutral, or Irrelevant
4. `Tweet` — social-media text

## Work performed

- Loaded and inspected the dataset
- Removed rows with missing topic, sentiment, or tweet text
- Normalized sentiment labels
- Cleaned tweet text by removing URLs, mentions, hashtags, punctuation, and extra spaces
- Explored overall sentiment distribution
- Compared sentiment across the top 10 topics/entities
- Examined tweet-length patterns by sentiment
- Extracted frequently occurring words for each sentiment
- Saved cleaned data, summary metrics, and visualizations

## Visualizations

- Overall sentiment distribution
- Sentiment distribution across top 10 topics
- Tweet-length distribution by sentiment

## Files

- `task04.py` — main Python analysis script
- `Task-04.ipynb` — Jupyter Notebook
- `outputs/` — generated charts and CSV summaries

## Requirements

Python 3.x with:

- pandas
- matplotlib

Run:

```bash
python task04.py
```

## Note

The analysis is descriptive. The sentiment labels in the supplied dataset are used as provided; the project does not claim to independently reclassify the original posts.
