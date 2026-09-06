# Stochastic Gradient Descent on Linear Regression

## Project Overview

This project uses machine learning to predict gym attendance based on historical gym usage data.

The main goal is to predict the number of people at the gym and identify patterns that can help determine less crowded times.

## Dataset

The dataset contains historical gym attendance records with features such as:

- Timestamp
- Temperature
- Day of the week
- Weekend indicator
- Holiday indicator
- Semester information
- Month
- Hour

The target variable is:

- `number_people`

## Models

Two main approaches were explored:

1. Stochastic Gradient Descent Linear Regression
2. Random Forest Regressor

The Random Forest model was further optimized using 5-fold Cross-Validation and GridSearchCV.

## Results

| Model | MAE | RMSE | R² |
|---|---:|---:|---:|
| SGD Linear Regression | 12.12 | 15.87 | 0.513 |
| Random Forest | 4.36 | 6.55 | 0.917 |
| Tuned Random Forest | 4.35 | 6.54 | 0.917 |

The Random Forest model significantly outperformed the SGD Linear Regression baseline, suggesting that gym attendance contains nonlinear relationships that are better captured by tree-based models.

## Tools & Libraries

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Jupyter Notebook