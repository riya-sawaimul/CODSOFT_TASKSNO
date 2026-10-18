# CODSOFT Data Analytics Internship - Task 1

## Task: Data Cleaning and Preprocessing

This project is completed as part of the CODSOFT Data Analytics Internship.

### Objective

The objective of this task is to import a dataset using Python, inspect its structure, identify missing values and duplicate records, clean the data, and prepare it for further analysis using Pandas.

### Dataset

Dataset used: Titanic Dataset

### Work Performed

- Imported the Titanic dataset using Pandas.
- Inspected the first few rows of the dataset.
- Checked the dataset shape and information.
- Identified missing values.
- Checked for duplicate records.
- Checked the data types of columns.
- Filled missing values in the `Age` column using the median.
- Removed the `Cabin` column because it contained a large number of missing values.
- Filled missing values in the `Embarked` column using the most frequent value.
- Verified that the cleaned dataset contains no remaining missing values.
- Saved the cleaned dataset as `Titanic_cleaned.csv`.

### Files

- `Titanic.csv` - Original dataset
- `Titanic_cleaned.csv` - Cleaned dataset
- `task1_data_cleaning.py` - Python code used for data cleaning

### Tools and Technologies

- Python
- Pandas
- VS Code

### Result

The Titanic dataset was successfully cleaned and prepared for further data analysis.