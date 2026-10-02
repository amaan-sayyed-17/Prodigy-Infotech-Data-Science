from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

DATA_URL = "https://raw.githubusercontent.com/Prodigy-InfoTech/data-science-datasets/main/Task%202/train.csv"
BASE = Path(__file__).resolve().parent
OUTPUT = BASE / "outputs"
OUTPUT.mkdir(exist_ok=True)

df = pd.read_csv(DATA_URL)

print("Original shape:", df.shape)
print("\nMissing values before cleaning:")
print(df.isnull().sum())

cleaned = df.copy()
cleaned["Age"] = cleaned["Age"].fillna(cleaned["Age"].median())
cleaned["Embarked"] = cleaned["Embarked"].fillna(cleaned["Embarked"].mode()[0])
cleaned["CabinKnown"] = cleaned["Cabin"].notna().astype(int)
cleaned = cleaned.drop(columns=["Cabin"])

cleaned.to_csv(OUTPUT / "titanic_cleaned.csv", index=False)

print("\nMissing values after cleaning:")
print(cleaned.isnull().sum())

survival_counts = cleaned["Survived"].value_counts().sort_index()
plt.figure(figsize=(7, 5))
plt.bar(["Did not survive", "Survived"], [survival_counts.get(0, 0), survival_counts.get(1, 0)])
plt.ylabel("Number of passengers")
plt.title("Titanic Survival Distribution")
plt.tight_layout()
plt.savefig(OUTPUT / "survival_distribution.svg", bbox_inches="tight")
plt.close()

survival_by_sex = cleaned.groupby("Sex")["Survived"].mean()
plt.figure(figsize=(7, 5))
plt.bar(survival_by_sex.index, survival_by_sex.values * 100)
plt.ylabel("Survival rate (%)")
plt.title("Titanic Survival Rate by Sex")
plt.tight_layout()
plt.savefig(OUTPUT / "survival_rate_by_sex.svg", bbox_inches="tight")
plt.close()

class_counts = cleaned["Pclass"].value_counts().sort_index()
plt.figure(figsize=(7, 5))
plt.bar(class_counts.index.astype(str), class_counts.values)
plt.xlabel("Passenger class")
plt.ylabel("Number of passengers")
plt.title("Passenger Distribution by Class")
plt.tight_layout()
plt.savefig(OUTPUT / "passenger_class_distribution.svg", bbox_inches="tight")
plt.close()

summary = pd.DataFrame({
    "metric": ["original_rows", "original_columns", "missing_age_before",
               "missing_embarked_before", "missing_cabin_before",
               "missing_values_after_cleaning"],
    "value": [len(df), len(df.columns), df["Age"].isna().sum(),
              df["Embarked"].isna().sum(), df["Cabin"].isna().sum(),
              int(cleaned.isna().sum().sum())]
})
summary.to_csv(OUTPUT / "eda_summary.csv", index=False)

print("\nEDA complete. Outputs saved in the outputs folder.")
