# pip is a pythons tool for installing packages
# pip stands for pip installs packages
#

# PyPi is the Python Package Index, a repository of software for the Python programming language.
# it is a collection of software written in the Python programming language that is available for download and installation.
#  pip automatically pulls packages from PyPi


# Popular Extra Python Libraries:

# TensorFlow – For machine learning and deep learning.

# Matplotlib – For creating charts and graphs.

# Pandas – For handling and analyzing data.

# NumPy – This is for working with numbers and large arrays.

# SciPy – For scientific and technical computing.

# Scrapy – For web scraping (getting data from websites).

# Scikit-learn – For machine learning (like predictions and classifications).

# PyGame – For building games with graphics and sound.

# PyTorch – For deep learning and neural networks.

# PyBrain – For beginners in machine learning and AI.


# Numpy stands for Numerical Python, it is a library for the Python programming language, adding support for
#  large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions
#  to operate on these arrays.


# pip install numpy

import numpy as np
# Create a  array
my_array = np.array([1, 2, 3, 4, 5])
print("Array:", my_array)


# pandas is a library for the Python programming language that provides data structures and data analysis tools.
# It is built on top of the NumPy library and is designed to make data manipulation and analysis easier and more efficient.
# Pandas is particularly useful for working with structured data, such as tabular data (like spreadsheets or SQL tables) and time series data.

import pandas as pd
# create a dataframe (table_like structure)

data = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'score': [85.5, 90.0, 78.5]
}

df = pd.DataFrame(data)
print("DataFrame:\n", df)

# accessing a column
print("Names:", df['name'])

# accessing a row
print('scores above 90:')
print( df[df['score'] > 90])

# matplotlib is a library for the Python programming language that provides tools for creating static, animated, and interactive visualizations in Python.
# It is widely used for data visualization and is particularly useful for creating plots, charts, and graphs.

import matplotlib.pyplot as plt
# Create some data
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]    

# Create a simple line plot
plt.plot(x, y, marker='o')
plt.title('Simple Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')    
plt.show()  # Display the plot


# Bar chart example
names = ['A', 'B', 'C', 'D']
values = [10, 20, 15, 25]

plt.bar(names, values )
plt.title('Bar Chart Example')
plt.xlabel('Names')
plt.ylabel('Values')
plt.show()  # Display the bar chart


# pie chart example
sizes = [15, 30, 45, 10]
labels = ['A', 'B', 'C', 'D']
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title('Pie Chart Example')
plt.show()  # Display the pie chart


# histogram example
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5]
plt.hist(data, bins=5, edgecolor='black')
plt.title('Histogram Example')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()  # Display the histogram

# combine with pandas 
import pandas as pd
import matplotlib.pyplot as plt 
# Create a DataFrame
data = {
    'Category': ['A', 'B', 'C', 'D'],
    'Values': [10, 20, 15, 25]
}
df = pd.DataFrame(data) 

# plot uisng pandas and matplotlib
plt.plot(df['Category'], df['Values'], marker='o')
plt.title('Pandas and Matplotlib Example')
plt.xlabel('Category')
plt.ylabel('Values')
plt.show()  # Display the plot
