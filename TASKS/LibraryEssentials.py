# -*- coding: utf-8 -*-
"""
# **`NumPy TASKS`**
"""

import numpy as np

# linear arrays with 20 random elements each ranging from 1 to 100

a = np.random.randint(1, 100, 20)
print(a)
b = np.random.randint(1, 100, 20)
print(b)

# changing a and b to two 5*4 matrices

a = a.reshape(5, 4)
b = b.reshape(5, 4)
print(a)
print(b)

#scalar multiplication

scaleA = 10
scaled_a = a * scaleA
print(scaled_a)
scaleB = 20
scaled_b = b * scaleB
print(scaled_b)

#modified b and matrixMul between a and b
modB = b.T
print(b)

c = np.dot(a, modB)
print(c)

#slicing techniques

print(c[:, 2:4]) # 0 based indexing
print('##')
print(c[:])

# max min and indexing

maxElem = np.max(c)
print(maxElem)

minElem = np.min(c)
print(minElem)

#index of the maxElem
maxIndex = np.argmax(c)
print(maxIndex)

# flattening arrays

cFlattened = c.flatten()
print(cFlattened)
print('---')
print(c)

"""# **`pandas TASKS`**"""

import pandas as pd

path = "/content/subject_scores.csv"
#reading the dataset
df = pd.read_csv(path)
print(df)

#first 5 rows
df.head(5)

#summary
df.info()

#how many null values we have in each column
df.isnull().sum()

# filling out a column's null values with the mean value of that particular column
df['Math']=df['Math'].fillna(df['Math'].mean())
df.isnull().sum()

# only the math scores of all students
print(df['Math'])

"""# **`Matplotlib TASKS`**"""

import matplotlib.pyplot as plt

temperature_dhaka = [25,34,21,45,28,6,43,18,7,2]
humidity_dhaka = [28, 25,29,20, 26, 50, 19, 29, 52, 55]

plt.scatter(temperature_dhaka, humidity_dhaka, marker='*', color='red')
plt.title("Temperature vs Humidity (Dhaka)")
plt.xlabel("Temperature (°C)")
plt.ylabel("Humidity (%)")
plt.show()

study_hours = [2,3,4,4, 5, 6, 7, 7, 8, 9, 9, 10, 11, 11, 12]
marks = [6, 10, 15, 20, 34, 44, 55, 60, 55, 67, 70, 80, 90, 99, 100]

plt.plot(study_hours, marks, color='red', marker='o')
plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.grid(True)
plt.show()

subjects = ['Maths', 'English', 'Science', 'Physics', 'Computer']
marks = [89, 90, 45, 78, 99]

plt.barh(subjects, marks, color='red')
plt.title("Subject Scores (Horizontal Bar)")
plt.xlabel("Marks")
plt.show()

plt.bar(subjects, marks, color=['red', 'blue', 'green', 'gray', 'orange'])
plt.title("Subject Scores (Vertical Bar)")
plt.ylabel("Marks")
plt.show()

temperature_dhaka = [25,34,21,45,28,6,43,18,7,2]
humidity_dhaka = [28, 25,29,20, 26, 50, 19, 29, 52, 55]
plt.subplot(2,2,1)
plt.scatter(temperature_dhaka, humidity_dhaka, marker='*', color='red')
plt.title("Temperature vs Humidity (Dhaka)")
plt.xlabel("Temperature (°C)")
plt.ylabel("Humidity (%)")

study_hours = [2,3,4,4, 5, 6, 7, 7, 8, 9, 9, 10, 11, 11, 12]
marks = [6, 10, 15, 20, 34, 44, 55, 60, 55, 67, 70, 80, 90, 99, 100]
plt.subplot(2,2,2)
plt.plot(study_hours, marks, color='red', marker='o')
plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.grid(True)

subjects = ['Maths', 'English', 'Science', 'Physics', 'Computer']
marks = [89, 90, 45, 78, 99]
plt.subplot(2,2,3)
plt.barh(subjects, marks, color='red')
plt.title("Subject Scores (Horizontal Bar)")
plt.xlabel("Marks")

plt.subplot(2,2,4)
plt.bar(subjects, marks, color=['red', 'blue', 'green', 'gray', 'orange'])
plt.title("Subject Scores (Vertical Bar)")
plt.ylabel("Marks")


plt.tight_layout()
plt.show()