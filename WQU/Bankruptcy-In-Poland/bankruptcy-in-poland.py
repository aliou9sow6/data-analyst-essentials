import json;
import gzip;

import pandas as pd;


with open('poland_data/bankruptcy-in-poland.json', 'r') as read_file:
    poland_data = json.load(read_file)

print(type(poland_data)) # <class 'dict'>
print(poland_data.keys()) # dict_keys(['data', 'meta']) query, data, meta

# Convert to DataFrame
df = pd.DataFrame(poland_data)
print(df.head()).__format__ # Display the first 5 rows of the DataFrame
print(df.shape) # (1000, 2) - 1000 rows and 2 columns

def wrangle(filename) :
    with open(filename, 'r') as read_file:
        poland_data = json.load(read_file)
    df = pd.DataFrame(poland_data)
    return df

data = wrangle('poland_data/bankruptcy-in-poland.json')
print("\n'''''''''''''Function output: '''''''''''''\n") # Display the first 5 rows of the DataFrame
print(data.head())