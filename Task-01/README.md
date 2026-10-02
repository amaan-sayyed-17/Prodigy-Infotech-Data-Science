# Prodigy InfoTech Data Science Internship — Task 01

## Objective
Create a bar chart or histogram to visualize the distribution of a continuous variable. This task uses country population data.

## Dataset
Official Prodigy InfoTech Task 01 dataset:
https://github.com/Prodigy-InfoTech/data-science-datasets/tree/main/Task%201

The dataset is a World Bank population dataset. The script automatically detects the latest available year, cleans population values, and excludes aggregate/region rows.

## Analysis
- Load the population CSV with pandas.
- Identify the latest available population year.
- Convert population values to numeric.
- Exclude aggregate/region rows.
- Create a top-15 country population bar chart.
- Create a histogram showing the distribution of country populations.
- Save visualizations in `outputs/`.

## Files
- `task01.py` — runnable Python script.
- `Task-01.ipynb` — notebook containing the analysis and visualizations.
- `outputs/population_bar_chart.svg` — repository preview of the bar chart.
- `outputs/population_distribution_histogram.svg` — repository preview of the histogram.
- `outputs/top15_population.csv` — generated top-15 data.
- When `task01.py` is run, it also generates PNG versions of both charts.

## Libraries
- pandas
- matplotlib
- jupyter

## Run
```bash
pip install pandas matplotlib jupyter
python task01.py
```

The script downloads the official Task 01 dataset from the Prodigy InfoTech repository when it is run.
