import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame
data = {
    'name': ['John', 'Anna', 'Peter', 'Linda'],
    'age': [25, 36, 45, 32],
    'height': [1.75, 1.85, 1.70, 1.68],
    'weight': [70, 65, 80, 55],
    'married': [False, True, True, False],
    'children': [2, 3, 2, 0],
    'pet': [True, True, False, False],
    'car': ['BMW', 'Audi', 'Ford', 'Toyota'],
    'city': ['New York', 'Paris', 'Berlin', 'London']
}

df = pd.DataFrame(data)
# use groupby() to group the data by the column 'name'
# then use the mean() method to calculate the average age for each group
grouped = df.groupby('name')['age'].mean()
print(grouped)

# sort the grouped data in descending order
sorted_grouped = grouped.sort_values(ascending=False)

print("Sort the grouped data in decending order: ",end="\n")
print(sorted_grouped)

# plot the sorted data using a bar chart with matplotlib 
plt.bar(sorted_grouped.index, sorted_grouped)
plt.xlabel('Name')
plt.ylabel('Average age')
plt.title('Average age by name')
plt.show()