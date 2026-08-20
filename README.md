# Flight Operations Data Analysis

## Project Overview

This project performs a complete data analysis workflow on a **Flight Operations dataset** using Python and Pandas. The analysis focuses on understanding the dataset, cleaning and transforming data, selecting relevant information, and identifying useful patterns and insights.

## Objectives

* Load and understand the Flight Operations dataset.
* Inspect the structure, columns, and data types.
* Generate descriptive statistics.
* Select and filter relevant records.
* Sort data based on different attributes.
* Perform grouping and aggregation.
* Apply suitable data transformations.
* Identify meaningful patterns and trends.
* Extract important findings from the dataset.

## Technologies Used

* **Python**
* **Pandas**
* **NumPy**
* **Jupyter Notebook / VS Code**

## Project Structure

```text
Flight-Operations-Data-Analysis/
│
├── Flight_Operations_Analysis.ipynb
├── flight_operations.csv
└── README.md
```

## Analysis Workflow

The notebook follows these major steps:

1. **Import Libraries**

   * Import Pandas and other required libraries.

2. **Load Dataset**

   * Read the CSV file using `pd.read_csv()`.

3. **Dataset Exploration**

   * View the first and last records.
   * Check shape, columns, index, and data types.
   * Inspect missing values.

4. **Statistical Analysis**

   * Use `describe()` to understand numerical variables.

5. **Data Selection & Filtering**

   * Select specific columns.
   * Filter records using meaningful conditions.

6. **Sorting**

   * Sort records using relevant numerical and categorical columns.

7. **Grouping & Aggregation**

   * Use `groupby()` with functions such as:

     * `sum()`
     * `mean()`
     * `count()`
     * `min()`
     * `max()`

8. **Data Transformation**

   * Create or modify columns using Pandas operations.
   * Apply transformations where required.

9. **Insights & Findings**

   * Analyze the results and identify important patterns in flight operations.

## Key Pandas Concepts Demonstrated

```python
pd.read_csv()
df.head()
df.tail()
df.shape
df.columns
df.dtypes
df.info()
df.describe()
df.isnull().sum()
df.loc[]
df.iloc[]
df.sort_values()
df.groupby()
df.agg()
df.apply()
```

## How to Run

### Using VS Code

1. Install Python.
2. Install the required libraries:

```bash
pip install pandas numpy jupyter
```

3. Open the project folder in VS Code.
4. Open `Flight_Operations_Analysis.ipynb`.
5. Select a Python kernel.
6. Run the notebook cells sequentially.

### Using Jupyter Notebook

```bash
jupyter notebook
```

Open the notebook and execute the cells from top to bottom.

## Expected Outcome

The project provides a structured understanding of flight operations data and demonstrates how Pandas can be used to **explore, manipulate, summarize, and analyze real-world datasets**.

## Author

**Pratyush Sharma**
B.Tech – Computer Science & Engineering (AI & ML)
