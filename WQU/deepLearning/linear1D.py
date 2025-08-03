# Import libraries
import numpy as np
import matplotlib.pyplot as plt

# Define a 1D linear function
def linear_function_1D(x, slope=1, intercept=0):
    return slope * x + intercept # y = mx + b, where m is slope and b is intercept

# Create an array of x values
x = np.arange(0, 10, 0.1) # Generate values from 0 to 10 with a step of 0.01
print(f"x values: {x[:5]}...")  # Print first 5 x values for verification

# Set slope and intercept
slope = 3.0
intercept = 1.5

# Calculate y values using the linear function
y = linear_function_1D(x, slope, intercept)

# Plot the results
plt.figure(figsize=(10, 5))
plt.plot(x, y, label=f" slope={slope}, intercept={intercept}")
# y label
plt.axhline(0, color='black', lw=0.5, ls='--')
plt.xlabel('x')
plt.ylabel('y')
plt.title('1D Linear Function')
plt.legend()
plt.grid(True)
plt.show()  # Display the plot
