# Task 05 — US Traffic Accident Analysis

## Objective
Analyze the US Accidents dataset to identify patterns related to **time of day, day of week, month, weather conditions, accident severity, road features, states/cities, and geographic hotspots**.

## Dataset
This project uses the **US Accidents (2016–2023)** dataset by Sobhan Moosavi on Kaggle. The dataset covers 49 US states and contains accident records collected from February 2016 through March 2023. The Kaggle dataset page reports 7,728,394 accident records and describes the data as being collected from multiple traffic APIs. [Kaggle dataset](https://www.kaggle.com/sobhanmoosavi/us-accidents/metadata)

> The full source CSV is **not stored in this repository** because it is several gigabytes. The analysis was executed on Kaggle using the full dataset, then the resulting CSV summaries and SVG visualizations were exported here.

## Analysis performed
- Processed the full dataset in chunks of 100,000 rows to avoid loading the multi-gigabyte CSV into memory at once.
- Checked missing values for `Start_Time` and `Weather_Condition`.
- Analyzed accidents by hour, weekday, and month.
- Examined accident severity levels 1–4.
- Compared accident counts across states and cities.
- Examined weather-condition frequencies.
- Counted records associated with road features such as traffic signals, crossings, junctions, stops, railways, and bumps.
- Aggregated rounded latitude/longitude pairs to visualize geographic accident hotspots.

## Genuine execution summary

| Metric | Result |
|---|---:|
| Total records processed | 7,728,394 |
| Missing `Start_Time` | 0 |
| Missing `Weather_Condition` | 173,459 |
| Unique states | 49 |
| Unique cities | 13,678 |
| Unique weather conditions | 144 |
| Average accident distance | 0.562 miles |

## Selected results

### Top states by accident count

| State | Accidents |
|---|---:|
| CA | 1,741,433 |
| FL | 880,192 |
| TX | 582,837 |
| SC | 382,557 |
| NY | 347,960 |
| NC | 338,199 |
| VA | 303,301 |
| PA | 296,620 |
| MN | 192,084 |
| OR | 179,660 |

### Top weather conditions

| Weather condition | Accidents |
|---|---:|
| Fair | 2,560,802 |
| Mostly Cloudy | 1,016,195 |
| Cloudy | 817,082 |
| Clear | 808,743 |
| Partly Cloudy | 698,972 |
| Overcast | 382,866 |
| Light Rain | 352,957 |
| Scattered Clouds | 204,829 |
| Light Snow | 128,680 |
| Fog | 99,238 |

### Time and weekday patterns
The exported results show that accident counts vary substantially by hour and day. The hourly CSV and chart provide the complete 24-hour distribution. The weekday results show the highest count on Friday (1,181,970) and lower counts on Saturday (540,244) and Sunday (459,398). These are descriptive accident-record patterns and do not by themselves establish causation or risk rates.

### Severity

| Severity | Accidents |
|---:|---:|
| 1 | 67,366 |
| 2 | 6,156,981 |
| 3 | 1,299,337 |
| 4 | 204,710 |

## Output files
- `eda_summary.csv` — execution summary
- `accidents_by_hour.csv` / `.svg` — hourly distribution
- `accidents_by_weekday.csv` / `.svg` — weekday distribution
- `accidents_by_month.csv` — monthly distribution
- `severity_distribution.csv` / `.svg` — severity distribution
- `top_states.csv` / `.svg` — top states
- `top_cities.csv` — top cities
- `top_weather_conditions.csv` / `.svg` — top weather conditions
- `road_features.csv` / `.svg` — road-feature counts
- `top_accident_hotspots.csv` / `accident_hotspots.svg` — geographic hotspot aggregation

## Reproducibility
The included `task05.py` searches for `US_Accidents_March23.csv`, reads it in chunks, computes the summaries, and writes the CSV outputs. The full source dataset should be attached to a Kaggle Notebook before running the script.

## Tools
Python · Pandas · Matplotlib · Jupyter/Kaggle Notebook
