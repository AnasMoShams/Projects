Predicting Car Prices

A Machine Learning project for predicting car market prices using the K-Nearest Neighbors (KNN) Regression algorithm.

This project focuses not only on building a predictive model, but also on understanding and applying the complete machine learning workflow: data preparation, exploratory analysis, feature scaling, train-test splitting, cross-validation, hyperparameter tuning, and final model evaluation.

💡 Project Idea

The idea for this project was inspired by the Dataquest Guided Project — Predicting Car Prices.

The original project introduces a machine learning workflow using K-Nearest Neighbors in R to predict car prices based on different vehicle characteristics.

I decided to recreate and implement the project in Python, while focusing on understanding the reasoning behind each step of the machine learning process rather than simply reproducing the original solution.

Original Project:
{"fallbackMarkdown":"Dataquest — Predicting Car Prices
","reference":{"matched_text":"","prefix":null,"start_idx":1486,"end_idx":1599,"safe_urls":[],"refs":[],"alt":"Dataquest — Predicting Car Prices
","prompt_text":null,"type":"url","layout":null,"item":{"title":"Dataquest — Predicting Car Prices","url":"https://www.dataquest.io/projects/guided-project-a-predicting-car-prices/?utm_source=chatgpt.com","attribution":"dataquest.io","pub_date":null,"snippet":null,"attribution_segments":null,"supporting_websites":[],"refs":[],"hue":null,"attributions":null},"logo":null,"title":"Dataquest — Predicting Car Prices"},"showLoginRequiredCard":false}

About Project

The dataset contains information about automobiles, including characteristics such as:

Engine size
Horsepower
Vehicle dimensions
Curb weight
Fuel economy
Compression ratio
Wheel base
And other numerical vehicle characteristics

The objective is to use these features to predict the market price (price) of a car.

The project follows a structured Machine Learning workflow:

Raw Dataset
     ↓
Data Cleaning
     ↓
Feature Selection
     ↓
Exploratory Analysis
     ↓
Train / Test Split
     ↓
Feature Scaling
     ↓
KNN + Cross-Validation
     ↓
Hyperparameter Tuning
     ↓
Final Evaluation

Problem

The problem is a supervised regression problem.

Given a set of numerical characteristics describing a car, we want to estimate its market price.

Input

Vehicle characteristics such as:

Engine Size
Horsepower
Curb Weight
Width
Length
Height
City MPG
Highway MPG
...

Target
price


The main challenge is that KNN is a distance-based algorithm, meaning that differences in feature scales can significantly affect the model.

For this reason, feature scaling is an important part of the preprocessing workflow.

🛠️ What I Did
1. Data Loading & Cleaning
Loaded the raw automobile dataset using Pandas.
Assigned meaningful column names based on the dataset documentation.
Converted ? values into NaN.
Selected numeric columns suitable for the KNN model.
Removed observations containing missing values as required by the project workflow.
2. Exploratory Analysis

Examined relationships between the numerical predictors using a correlation matrix.

This helped identify:

Strong relationships between predictors.
Potentially redundant information.
Relationships between predictors and the target variable.
3. Train-Test Split

The dataset was divided into:

80% Training Data
20% Test Data

The test set was kept unseen during model selection and hyperparameter tuning.

4. Feature Scaling

Since KNN relies on distance calculations, the features were standardized using:

StandardScaler


The scaler was fitted on the training data and then used to transform the test data.

5. Cross-Validation & Hyperparameter Tuning

Used 5-fold cross-validation with GridSearchCV to search for the optimal number of neighbors.

The tested range was:

K = 1 ... 20


The best-performing configuration was:

K = 1

6. Final Model Evaluation

The final model was evaluated on the unseen test set using:

Mean Squared Error (MSE)
Root Mean Squared Error (RMSE)
Mean Absolute Error (MAE)
R² Score
What Came of It

The final KNN model achieved the following results on the test set:

Metric	Score
MSE	5,830,649.63
RMSE	2,414.67
MAE	1,725.25
R²	0.6723
Interpretation

The model achieved an R² score of approximately 0.67, meaning it explains around 67% of the variation in car prices in the test set.

The MAE of approximately 1,725 means that, on average, the model's absolute prediction error was around 1,725 price units.

The selected value of:

K = 1


performed best during cross-validation among the tested values.

However, because the dataset is relatively small and K=1 produces a highly local model, further experimentation would be useful before considering this the optimal real-world solution.

Technologies

The project was implemented in Python using the following tools and libraries:

Python — Main programming language
Pandas — Data loading, cleaning, and manipulation
NumPy — Numerical computations
Matplotlib — Data visualization
Scikit-learn — Machine learning, preprocessing, cross-validation, hyperparameter tuning, and evaluation
Jupyter Notebook — Interactive development and documentation
Machine Learning Concepts Practiced

This project was used to practice several important Machine Learning concepts:

Supervised Learning
Regression
K-Nearest Neighbors
Feature Scaling
Correlation Analysis
Train-Test Split
K-Fold Cross-Validation
Hyperparameter Optimization
Data Leakage Prevention
Model Evaluation
Generalization
Future Improvements

There are several ways this project could be extended:

Experiment with different feature-selection strategies.
Compare StandardScaler, MinMaxScaler, and RobustScaler.
Investigate imputation strategies instead of removing missing observations.
Experiment with different distance metrics for KNN.
Test different regression algorithms.
Perform more extensive hyperparameter tuning.
Investigate the effect of outliers on model performance.
Evaluate model stability using repeated cross-validation.
Reference

This project was inspired by the following Dataquest guided project:

{"fallbackMarkdown":"Predicting Car Prices — Dataquest
","reference":{"matched_text":"","prefix":null,"start_idx":6576,"end_idx":6689,"safe_urls":[],"refs":[],"alt":"Predicting Car Prices — Dataquest
","prompt_text":null,"type":"url","layout":null,"item":{"title":"Predicting Car Prices — Dataquest","url":"https://www.dataquest.io/projects/guided-project-a-predicting-car-prices/?utm_source=chatgpt.com","attribution":"dataquest.io","pub_date":null,"snippet":null,"attribution_segments":null,"supporting_websites":[],"refs":[],"hue":null,"attributions":null},"logo":null,"title":"Predicting Car Prices — Dataquest"},"showLoginRequiredCard":false}

The original project focuses on applying the machine learning workflow with K-Nearest Neighbors to predict car prices. This repository is an independent Python implementation and learning exercise based on that project.