# Task 04 — Sentiment Analysis and Visualization

**Prodigy InfoTech Data Science Internship**

## Objective

Analyze and visualize sentiment patterns in social media data to understand public opinion and attitudes toward specific topics or brands.

## Dataset

Official Prodigy InfoTech dataset:
`Task 4/twitter_training.csv`

Columns:
- `ID` — tweet identifier
- `Topic` — topic/entity mentioned in the post
- `Sentiment` — Positive, Negative, Neutral, or Irrelevant
- `Tweet` — original social-media text

## Work performed

1. Loaded the official training CSV.
2. Checked missing values.
3. Removed records with missing topic, sentiment, or tweet text.
4. Normalized sentiment labels and removed empty/invalid sentiment records.
5. Cleaned tweet text by lowercasing and removing URLs, mentions, hashtags, punctuation, and extra whitespace.
6. Calculated tweet length after cleaning.
7. Visualized overall sentiment distribution.
8. Compared sentiment counts across the 10 most frequent topics/entities.
9. Visualized tweet-length distributions by sentiment.
10. Extracted frequent words for each sentiment category.

## Genuine execution results

The results below were generated from the official `twitter_training.csv` supplied by Prodigy InfoTech. No fabricated output values were added.

| Metric | Result |
|---|---:|
| Original rows | 74,682 |
| Missing tweet values | 686 |
| Rows after cleaning | 73,824 |
| Unique topics/entities | 32 |
| Positive posts | 20,619 |
| Negative posts | 22,312 |
| Neutral posts | 18,051 |
| Irrelevant posts | 12,842 |

### Top 10 topics by number of posts

| Topic | Posts |
|---|---:|
| LeagueOfLegends | 2,372 |
| CallOfDuty | 2,371 |
| MaddenNFL | 2,370 |
| Verizon | 2,361 |
| Facebook | 2,360 |
| Dota2 | 2,359 |
| WorldOfCraft | 2,356 |
| TomClancysRainbowSix | 2,354 |
| Microsoft | 2,349 |
| ApexLegends | 2,347 |

## Outputs

- `outputs/eda_summary.csv` — summary metrics
- `outputs/sentiment_distribution.svg` — overall sentiment chart
- `outputs/sentiment_by_topic.svg` — sentiment by top 10 topics
- `outputs/sentiment_by_topic.csv` — topic/sentiment counts
- `outputs/tweet_length_by_sentiment.svg` — tweet-length distributions
- `outputs/top_words_by_sentiment.csv` — frequent words by sentiment

## Reproducibility

`task04.py` loads the official Prodigy URL by default. It also accepts a local CSV path:

```bash
python task04.py path/to/twitter_training.csv
```

The notebook contains the same analysis workflow and the genuine results obtained from the supplied official dataset.

## Technologies

Python, Pandas, Matplotlib, Jupyter Notebook, Regular Expressions
