# 📌 Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 🎯 Task 1: Load and Explore the Dataset
try:
    # Load CSV dataset (replace 'dataset.csv' with your file)
    df = pd.read_csv('dataset.csv')
    
    # Display first 5 rows
    print("First 5 Rows of Dataset:")
    print(df.head())
    
    # Display info and check missing values
    print("\nDataset Info:")
    print(df.info())
    print("\nMissing Values:")
    print(df.isnull().sum())
    
    # Clean dataset (fill missing numerical values with mean)
    df.fillna(df.mean(numeric_only=True), inplace=True)
    # Drop rows if essential columns have missing values
    df.dropna(inplace=True)
    print("\nData cleaned successfully.")
    
except FileNotFoundError:
    print("Error: Dataset file not found. Please check the filename.")
except Exception as e:
    print(f"An error occurred: {e}")

# 🎯 Task 2: Basic Data Analysis
print("\nBasic Statistics:")
print(df.describe())

# Example: Grouping by a categorical column (modify to match your dataset)
if 'species' in df.columns:
    group_data = df.groupby('species')['sepal_length'].mean()
    print("\nAverage Sepal Length per Species:")
    print(group_data)

# 🎯 Task 3: Data Visualization

# 1️⃣ Line Chart (Example: Trends over time)
if 'date' in df.columns:
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date')['sales'].plot(kind='line')
    plt.title("Sales Trend Over Time")
    plt.xlabel("Date")
    plt.ylabel("Sales")
    plt.show()

# 2️⃣ Bar Chart (Example: Average petal length per species)
if 'species' in df.columns and 'petal_length' in df.columns:
    avg_petal = df.groupby('species')['petal_length'].mean()
    avg_petal.plot(kind='bar', color='skyblue')
    plt.title("Average Petal Length per Species")
    plt.xlabel("Species")
    plt.ylabel("Petal Length")
    plt.show()

# 3️⃣ Histogram (Distribution of a numerical column)
if 'sepal_length' in df.columns:
    plt.hist(df['sepal_length'], bins=10, color='lightgreen', edgecolor='black')
    plt.title("Distribution of Sepal Length")
    plt.xlabel("Sepal Length")
    plt.ylabel("Frequency")
    plt.show()

# 4️⃣ Scatter Plot (Relationship between two numerical columns)
if 'sepal_length' in df.columns and 'petal_length' in df.columns:
    plt.scatter(df['sepal_length'], df['petal_length'], color='purple')
    plt.title("Sepal Length vs Petal Length")
    plt.xlabel("Sepal Length")
    plt.ylabel("Petal Length")
    plt.show()

# 🎯 Findings (example)
print("\nObservations:")
print("- The dataset has been cleaned with missing values handled.")
print("- The histogram shows the distribution of Sepal Length.")
print("- The scatter plot suggests a correlation between Sepal and Petal lengths.")
print("- The bar chart compares average petal length per species.")

