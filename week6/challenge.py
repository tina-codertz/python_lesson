import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import requests 

# create a numpy array of numbers from 1 to 10 and calculate their mean
numbers = np.array(range(1,11))
mean_value = np.mean(numbers)
print("Mean of numbers from 1 to 10:", mean_value)


# loasd small dataset into pandas dataframe and display summary statics
data ={
    'name': ['asha', 'pob', 'Chale'],
    'age': [25, 30, 35],
    'score': [85.0, 90.0, 78]
}

df = pd.DataFrame(data)
print("DataFrame:\n", df)
print("Summary Statistics:\n", df.describe())

# fetch data from public api using requests library and print key piece of information
response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
if response.status_code == 200:
    post = response.json()
    print("Post Title:", post['title'])
else:
    print("Failed to retrieve data from API. Status code:", response.status_code)



# plot a simple line graph using matplotlib 
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y= [2, 3, 6, 8,9 ]

# create a simple lin
plt.plot(x, y, marker='o')
plt.title('simple plt')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()