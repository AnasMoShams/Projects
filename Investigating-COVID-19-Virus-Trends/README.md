
# Investigating COVID-19 Virus Trends

## About the Project

This project explores COVID-19 testing data to investigate which countries reported the highest test positivity rates.

Using Python, Pandas, and Matplotlib, the project focuses on data exploration, data cleaning, positivity rate calculation, and visualization. It also examines how missing values and inconsistent reporting dates affect comparisons between countries.

## Project Objective

The main objective is to identify countries with high COVID-19 test positivity rates based on the available testing data.

**Positivity Rate Formula:**

`Positivity Rate = (Positive Cases / Total Tests) × 100`

## Problem

The dataset contains several data quality challenges:

* Missing values in important columns.
* Repeated country-date records with conflicting values.
* Inconsistent reporting dates across countries.
* Countries with incomplete testing information.
* Limited ability to compare countries fairly when their latest valid records come from different dates.

These issues require careful data cleaning and interpretation before drawing conclusions.

## What I Did

1. Loaded the dataset and explored its structure using Pandas.
2. Inspected column data types, missing values, and duplicate records.
3. Converted date values into a proper datetime format.
4. Reviewed country-level records and standardized selected country names.
5. Investigated repeated country-date records before removing duplicates.
6. Selected the latest valid record containing both positive cases and total tests for each country.
7. Calculated positivity rates and ranked countries by their calculated rates.
8. Examined data recency and compared results within a shared recent time window.
9. Created a horizontal bar chart to visualize the top 10 countries.

## Key Findings

Using the latest available valid record for each country, the highest calculated positivity rates were:

| Country      | Record Date | Positivity Rate |
| ------------ | ----------- | --------------: |
| Tanzania     | 2020-05-09  |          78.07% |
| Burkina Faso | 2020-04-29  |          48.09% |
| Ecuador      | 2020-04-30  |          36.11% |
| Costa Rica   | 2020-11-06  |          35.04% |
| Mexico       | 2020-05-10  |          31.56% |

These results are based on the latest records where both positive cases and total tests were available. The record dates differ across countries, so this ranking should be interpreted as exploratory rather than a direct comparison of countries at the same point in time.

### Recent Time-Window Comparison

A separate analysis examined records from November 2 to November 9, 2020. Within this period, 97 countries had at least one record, but only 14 had valid values for both positive cases and total tests.

This limited coverage demonstrates the importance of considering data availability when comparing countries.

## Data Source

The dataset was provided for the Dataquest guided project:

[COVID-19 Dataset](https://dq-content.s3.amazonaws.com/505/covid19.csv)

The dataset contains country-level and regional COVID-19 reporting records, including positive cases, total tests, and other health-related measures.

## Technologies

* **Python** — Data analysis and scripting.
* **Pandas** — Data cleaning, manipulation, and analysis.
* **Matplotlib** — Data visualization.
* **Jupyter Notebook** — Interactive analysis and documentation.

## Limitations

* The dataset contains missing and inconsistent records.
* The latest valid record does not come from the same date for every country.
* Testing coverage and reporting practices may differ between countries.
* Test positivity rate is not the same as the percentage of the population infected.
* The results reflect the available historical dataset and should not be interpreted as current COVID-19 statistics.

## Conclusion

This project demonstrates a practical data analysis workflow, from exploring and cleaning a real-world dataset to calculating metrics and communicating findings through visualizations.

It also highlights why data quality, reporting consistency, and transparent methodology are essential for making meaningful comparisons.

---

**Project Type:** Data Analysis
**Dataset:** Historical COVID-19 testing data
**Language:** Python
