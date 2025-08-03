# Sample 3D linear Plane: y = b + m1*x + m2*z
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define a 3D linear function
def linear_function_3D(x, z, m1=1, m2=1, b=0):
    return b + m1 * x + m2 * z  # y = b + m1*x + m2*z

# Create a grid of x and z values
x = np.arange(-5, 5, 0.1)  # Generate values from -5 to 5 with a step of 0.1
z = np.arange(-5, 5, 0.1)  # Generate values from -5 to 5 with a step of 0.1
X, Z = np.meshgrid(x, z)  # Create a meshgrid for 3D plotting

print(f"x values: {X[0, :5]}...")  # Print first 5 x values for verification
print(f"z values: {Z[:5, 0]}...")  # Print first 5 z values for verification
# Set coefficients for the linear function
beta = -3
omega_1 = 1
omega_2 = 0
# Calculate y values using the linear function
Y = linear_function_3D(X, Z, m1=omega_1, m2=omega_2, b=beta)  

# Plotting the 3D surface
fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot(111, projection="3d")
ax.plot_surface(X, Z, Y, cmap='plasma', edgecolor='k', alpha=0.85)

# Labels and title
ax.set_xlabel('$x_1$')
ax.set_ylabel('$x_2$')
ax.set_zlabel('$y$')
ax.set_title('3D linear plane')

plt.tight_layout()
plt.show()