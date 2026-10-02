# Prodigy InfoTech Data Science Internship — Task 01
# Population Distribution Visualization

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

DATA_URL = (
    "https://raw.githubusercontent.com/Prodigy-InfoTech/"
    "data-science-datasets/main/Task%201/"
    "API_SP.POP.TOTL_DS2_en_csv_v2_38144.csv"
)

BASE = Path(__file__).resolve().parent
OUTPUT = BASE / "outputs"
OUTPUT.mkdir(exist_ok=True)

df = pd.read_csv(DATA_URL, skiprows=4)

year_columns = [c for c in df.columns if str(c).isdigit()]
latest_year = year_columns[-1]

aggregate_codes = {
    "AFE","AFW","ARB","CEB","CSS","EAR","EAS","ECA","ECS","EMU","EUU",
    "FCS","HIC","HPC","IBD","IBT","IDA","IDB","IDX","LAC","LCN","LDC",
    "LIC","LMC","LMY","LTE","MEA","MIC","MNA","NAC","OED","OSS","PRE",
    "PST","PSS","SSA","SSF","SST","TEA","TEC","TLA","TMN","TSA","TSS",
    "UMC","WLD"
}

population = df[~df["Country Code"].isin(aggregate_codes)][
    ["Country Name", "Country Code", latest_year]
].copy()
population[latest_year] = pd.to_numeric(population[latest_year], errors="coerce")
population = population.dropna(subset=[latest_year])

top15 = population.sort_values(latest_year, ascending=False).head(15)

plt.figure(figsize=(12, 7))
plt.bar(top15["Country Name"], top15[latest_year])
plt.xticks(rotation=55, ha="right")
plt.ylabel(f"Population ({latest_year})")
plt.xlabel("Country")
plt.title(f"Top 15 Countries by Population ({latest_year})")
plt.tight_layout()
plt.savefig(OUTPUT / "population_bar_chart.png", dpi=200, bbox_inches="tight")
plt.close()

plt.figure(figsize=(10, 6))
plt.hist(population[latest_year], bins=30)
plt.xlabel(f"Population ({latest_year})")
plt.ylabel("Number of countries")
plt.title(f"Distribution of Country Populations ({latest_year})")
plt.tight_layout()
plt.savefig(OUTPUT / "population_distribution_histogram.png", dpi=200, bbox_inches="tight")
plt.close()

top15.to_csv(OUTPUT / "top15_population.csv", index=False)

print(f"Task 01 completed using {latest_year} population data.")
print(top15[["Country Name", latest_year]].to_string(index=False))
