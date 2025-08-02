# Goals : Work with the database(sqlite) relationship without server directly, using python only
import sqlite3
import matplotlib.pyplot as plt
# This script demonstrates how to connect to a SQLite database, create tables, insert records,

# I. Create a connection to the SQLite database
# If the database does not exist, it will be created

conn = sqlite3.connect('test.db')
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER, name TEXT)")
# I.1. Insert a record into the table if it does not exist
cursor.execute("INSERT OR IGNORE INTO users VALUES (?, ?)", (1, 'Alice'))
# I.2. Insert many records at once
cursor.executemany("INSERT OR IGNORE INTO users VALUES (?, ?)", [(2, 'Bob'), (3, 'Charlie'), (4, 'David'), (5, 'Eve')])
# I.3. Commit the changes to the database
conn.commit()

cursor.execute("SELECT * FROM users") # Query the database to verify the records
rows = cursor.fetchall() # Fetch all rows from the query
for row in rows:
    print(row)

# I.5. Create a table if it does not exist
# I.6. Create a table with a primary key
cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    price REAL NOT NULL
)""")   
# I.4. Close the connection
conn.close()

# II. matplotlib.pyplot, Visualize the data
# Reconnect to the database
conn = sqlite3.connect('test.db')
cursor = conn.cursor()

# Insert sample data into the products table
cursor.executemany("INSERT OR IGNORE INTO products (id, name, price) VALUES (?, ?, ?)", 
               [(1, 'Product A', 10.99), (2, 'Product B', 15.49), 
                (3, 'Product C', 7.99), (4, 'Product D', 12.99), 
                (5, 'Product E', 9.99), (6, 'Product F', 20.00)
            ])    
# Commit the changes to the database
conn.commit()
# and visualize the data using matplotlib.
# Fetch data for visualization
cursor.execute("SELECT * FROM products")
products = cursor.fetchall()  # Fetch all products from the database
for product in products:
    print(product)

# Prepare data for plotting
product_names = [product[1] for product in products]  # Extract product names
product_prices = [product[2] for product in products]  # Extract product prices
# Create a bar chart
plt.bar(product_names, product_prices, color='blue')
plt.xlabel('Product Name')
plt.ylabel('Price')
plt.title('Product Prices')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust layout to prevent clipping of tick-labels
plt.show()  # Display the plot
