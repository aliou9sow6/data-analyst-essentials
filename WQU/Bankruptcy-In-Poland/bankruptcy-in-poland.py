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
print("\n'''''''''''''DataFrame shape: '''''''''''''\n") # Display the shape of the DataFrame
print(data.shape) # (1000, 2) - 1000 rows and 2 columns
# Save DataFrame to CSV
data.to_csv('poland_data/bankruptcy-in-poland.csv', index=False)
# Save DataFrame to GZIP CSV
data.to_csv('poland_data/bankruptcy-in-poland.csv.gz', index=False, compression='gzip')

# Read the GZIP CSV file
data_gzip = pd.read_csv('poland_data/bankruptcy-in-poland.csv.gz', compression='gzip')
print("\n'''''''''''''GZIP CSV DataFrame shape: '''''''''''''\n") # Display the shape of the DataFrame
print(data_gzip.shape) # (1000, 2) - 1000 rows and 2 columns

# More information about the dataset
print("\n'''''''''''''DataFrame info: '''''''''''''\n") # Display the info of the DataFrame
print(data_gzip.info().__format__) # Display the info of the DataFrame

print("\n'''''''''''''DataFrame columns: '''''''''''''\n") # Display the columns of the DataFrame
print(data_gzip.columns) # Index(['query', 'data'], dtype='object') - 2 columns: query and data

print("\n'''''''''''''DataFrame dtypes: '''''''''''''\n") # Display the dtypes of the DataFrame
print(data_gzip.dtypes) # query: object, data: object - both columns are of type object

print("\n'''''''''''''DataFrame describe(include='all'): '''''''''''''\n") # Display the description of the DataFrame
print(data_gzip.describe(include='all')) # Display the description of the DataFrame including all columns

