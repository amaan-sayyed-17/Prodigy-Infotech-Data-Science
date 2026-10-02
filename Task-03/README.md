# Task 03 - Decision Tree Classifier

## Objective

Build a decision tree classifier to predict whether a customer will purchase a product or service based on demographic and behavioral data.

## Dataset

Official Prodigy InfoTech Task 03 Bank Marketing dataset:

https://github.com/Prodigy-InfoTech/data-science-datasets/tree/main/Task%203

The script uses `Task 3/bank/bank.csv`, a smaller version of the Bank Marketing dataset, so the project remains easy to reproduce.

The original dataset is from the UCI Machine Learning Repository. The classification target is `y`, indicating whether the client subscribed to a term deposit.

## What I did

- Loaded the Bank Marketing dataset.
- Separated features from the target variable.
- Encoded categorical variables using One-Hot Encoding.
- Split the data into training and testing sets using an 80/20 stratified split.
- Built a Decision Tree Classifier using scikit-learn.
- Limited tree depth to 5 to keep the model interpretable and reduce overfitting.
- Evaluated the model using:
  - Accuracy
  - Precision
  - Recall
  - F1-score
  - Confusion matrix
- Visualized feature importance and the first levels of the decision tree.

## Files

- `task03.py` - complete Python implementation.
- `Task-03.ipynb` - Jupyter Notebook version.
- `outputs/model_metrics.csv` - model evaluation metrics after running the script.
- `outputs/confusion_matrix.svg` - confusion matrix.
- `outputs/feature_importance.svg` - top feature importances.
- `outputs/top_feature_importance.csv` - feature importance data.
- `outputs/decision_tree.svg` - visualization of the first three tree levels.

## Requirements

- Python 3.x
- pandas
- matplotlib
- scikit-learn

Install:

```bash
pip install pandas matplotlib scikit-learn
```

Run:

```bash
python task03.py
```

## Reference

UCI Machine Learning Repository - Bank Marketing:

https://archive.ics.uci.edu/dataset/222/bank+marketing
