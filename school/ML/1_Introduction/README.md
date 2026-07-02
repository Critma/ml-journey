# ML Journey - Lecture 1: Introduction to Data Analysis and Modeling

## Task Description

### Introduction
- Write 5 real-world examples of ML applications and explain the benefits of using ML in each.
- Classify tasks using the standard ML task taxonomy (classification, regression, clustering, etc.).
- Explain the difference between multiclass and multilabel classification.
- Determine whether the house price prediction example is a classification or regression problem, and discuss whether regression can be reduced to classification.

### Data Analysis
- Import required libraries: `pandas`, `numpy`, `sklearn`, `lightgbm`, `scipy`, `statsmodels`, `matplotlib`, `seaborn`.
- Load data from `train.json` (Kaggle dataset).
- Explore dataset size, columns, and identify the target column.
- Perform quick analysis using `info()`, `describe()`, and `corr()` methods.
- Create a reduced dataframe with columns: `bathrooms`, `bedrooms`, `interest_level`, and target `price`.

### Statistical Analysis
- Review basic statistics: mean, median, mode, variance, standard deviation.
- Understand distributions (uniform, Bernoulli, binomial, Poisson, normal, exponential).
- Identify outliers, percentiles, and confidence intervals.
- Analyze the target variable (price) using histograms and boxplots; handle outliers by dropping rows outside 1st and 99th percentiles.

### Feature Analysis
- Determine the type of `interest_level` column and count occurrences of each value.
- Encode categorical values (e.g., 0, 1, 2).
- Plot histograms for `bathrooms` and `bedrooms`; check for outliers.
- Compute and visualize the correlation matrix (heatmap) and scatterplots for features vs. target.

### Feature Engineering
- Create squared features: `bathrooms_squared`, `bedrooms_squared`, `interest_level_squared`.
- Compute new correlation matrix and compare with original features.
- Read train/test split data (already provided).
- Apply `PolynomialFeatures` with degree 10 to transform features.

### Modeling
- Train three models: linear regression, decision tree regressor (random_state=21), and naive models (mean/median).
- Evaluate using MAE and RMSE on train and test sets.
- Store results in two DataFrames: `result_MAE` and `result_RMSE`.

### Comparison
- Print final results tables and identify the best-performing model.