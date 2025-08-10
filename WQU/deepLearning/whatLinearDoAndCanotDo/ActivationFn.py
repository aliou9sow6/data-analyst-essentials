import torch
import matplotlib.pyplot as plt

# Create a range of x values
x_vals = torch.linspace(-5, 5, 100)

# Compute outputs
relu = torch.relu(x_vals)
sigmoid = torch.sigmoid(x_vals)
tanh = torch.tanh(x_vals)

# Plot all three functions
plt.figure(figsize=(15, 4))

# ReLU
plt.subplot(1, 3, 1)
plt.plot(x_vals.numpy(), relu.numpy())
plt.title('ReLU Activation')
plt.xlabel('x')
plt.ylabel('ReLU(x)')
plt.grid(True)

# Sigmoid
plt.subplot(1, 3, 2)
plt.plot(x_vals.numpy(), sigmoid.numpy())
plt.title('Sigmoid Activation')
plt.xlabel('x')
plt.ylabel('Sigmoid(x)')
plt.grid(True)

# Tanh
plt.subplot(1, 3, 3)
plt.plot(x_vals.numpy(), tanh.numpy())
plt.title('Tanh Activation')
plt.xlabel('x')
plt.ylabel('Tanh(x)')
plt.grid(True)

plt.tight_layout()
plt.show()
