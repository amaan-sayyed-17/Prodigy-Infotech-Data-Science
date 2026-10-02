from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    ConfusionMatrixDisplay,
    precision_score,
    recall_score,
    f1_score,
)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.tree import DecisionTreeClassifier, plot_tree

DATA_URL = (
    "https://raw.githubusercontent.com/Prodigy-InfoTech/"
    "data-science-datasets/main/Task%203/bank/bank.csv"
)

BASE = Path(__file__).resolve().parent
OUTPUT = BASE / "outputs"
OUTPUT.mkdir(exist_ok=True)

# Load the official Prodigy InfoTech Task 03 dataset.
df = pd.read_csv(DATA_URL, sep=";")

print("Dataset shape:", df.shape)
print("\nTarget distribution:")
print(df["y"].value_counts())

# Separate features and target.
X = df.drop(columns=["y"])
y = df["y"].map({"no": 0, "yes": 1})

categorical_features = X.select_dtypes(include=["object"]).columns.tolist()
numeric_features = X.select_dtypes(exclude=["object"]).columns.tolist()

preprocessor = ColumnTransformer(
    transformers=[
        ("categorical", OneHotEncoder(handle_unknown="ignore"), categorical_features),
        ("numeric", "passthrough", numeric_features),
    ]
)

model = DecisionTreeClassifier(
    criterion="gini",
    max_depth=5,
    random_state=42,
)

pipeline = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("classifier", model),
    ]
)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y,
)

pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, zero_division=0)
recall = recall_score(y_test, y_pred, zero_division=0)
f1 = f1_score(y_test, y_pred, zero_division=0)

print("\nModel performance:")
print(f"Accuracy : {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall   : {recall:.4f}")
print(f"F1-score : {f1:.4f}")

print("\nClassification report:")
print(classification_report(y_test, y_pred, target_names=["No", "Yes"], zero_division=0))

# Save evaluation metrics.
metrics = pd.DataFrame(
    {
        "metric": ["accuracy", "precision", "recall", "f1_score"],
        "value": [accuracy, precision, recall, f1],
    }
)
metrics.to_csv(OUTPUT / "model_metrics.csv", index=False)

# Confusion matrix.
cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["No", "Yes"])
disp.plot()
plt.title("Bank Marketing Decision Tree - Confusion Matrix")
plt.tight_layout()
plt.savefig(OUTPUT / "confusion_matrix.svg", bbox_inches="tight")
plt.close()

# Feature importance after one-hot encoding.
feature_names = pipeline.named_steps["preprocessor"].get_feature_names_out()
importances = pipeline.named_steps["classifier"].feature_importances_

importance_df = (
    pd.DataFrame({"feature": feature_names, "importance": importances})
    .sort_values("importance", ascending=False)
    .head(15)
)

importance_df.to_csv(OUTPUT / "top_feature_importance.csv", index=False)

plt.figure(figsize=(10, 7))
plt.barh(
    importance_df["feature"].iloc[::-1],
    importance_df["importance"].iloc[::-1],
)
plt.xlabel("Importance")
plt.ylabel("Feature")
plt.title("Top 15 Decision Tree Feature Importances")
plt.tight_layout()
plt.savefig(OUTPUT / "feature_importance.svg", bbox_inches="tight")
plt.close()

# Visualize the first levels of the trained decision tree.
encoded_X_train = pipeline.named_steps["preprocessor"].transform(X_train)

plt.figure(figsize=(22, 12))
plot_tree(
    pipeline.named_steps["classifier"],
    feature_names=feature_names,
    class_names=["No", "Yes"],
    filled=True,
    max_depth=3,
    fontsize=7,
)
plt.title("Decision Tree Classifier (First 3 Levels)")
plt.tight_layout()
plt.savefig(OUTPUT / "decision_tree.svg", bbox_inches="tight")
plt.close()

print("\nTask 03 completed. Outputs saved in the outputs folder.")
