# DAV Experiment 1 - NumPy and Pandas

import numpy as np
import pandas as pd

# ---------------- NUMPY ----------------

print("========== NUMPY ==========")

# Creating an array
a = np.array([10, 20, 30, 40, 50])
print("Array:", a)

# Array attributes
print("Dimensions:", a.ndim)
print("Shape:", a.shape)
print("Size:", a.size)
print("Data type:", a.dtype)

# Indexing and slicing
print("First element:", a[0])
print("Last element:", a[-1])
print("Slicing:", a[1:4])

# Array operations
b = np.array([1, 2, 3, 4, 5])

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)

# Mathematical functions
print("Square root:", np.sqrt(a))
print("Square:", np.square(a))

# Statistical functions
print("Sum:", np.sum(a))
print("Mean:", np.mean(a))
print("Maximum:", np.max(a))
print("Minimum:", np.min(a))
print("Standard deviation:", np.std(a))

# Reshape
c = np.arange(1, 10)
print("Original:", c)
print("Reshaped:\n", c.reshape(3, 3))


# ---------------- PANDAS ----------------

print("\n========== PANDAS ==========")

# Creating a Series
marks = pd.Series([85, 90, 78, 92, 88])
print("Series:\n", marks)

# Creating a DataFrame
data = {
    "Name": ["Anu", "Bharath", "Chitra", "Deepak", "Esha"],
    "Age": [20, 21, 20, 22, 21],
    "Marks": [85, 90, 78, 92, 88]
}

df = pd.DataFrame(data)

print("\nDataFrame:")
print(df)

# DataFrame information
print("\nShape:", df.shape)
print("Columns:", df.columns)

# First and last rows
print("\nFirst 3 rows:")
print(df.head(3))

print("\nLast 2 rows:")
print(df.tail(2))

# Selecting columns
print("\nNames:")
print(df["Name"])

# Selecting rows
print("\nFirst row:")
print(df.iloc[0])

# Filtering
print("\nStudents with marks above 85:")
print(df[df["Marks"] > 85])

# Sorting
print("\nSorted by marks:")
print(df.sort_values("Marks", ascending=False))

# Statistical summary
print("\nStatistics:")
print(df["Marks"].describe())

# Add a new column
df["Result"] = ["Pass", "Pass", "Pass", "Pass", "Pass"]

print("\nUpdated DataFrame:")
print(df)

# Save as CSV
df.to_csv("students.csv", index=False)

print("\nData saved to students.csv")