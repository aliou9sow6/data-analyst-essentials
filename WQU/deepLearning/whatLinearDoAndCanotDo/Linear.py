import torch
import matplotlib.pyplot as plt

from noise import x, y

# Set random seed for reproducibility
torch.manual_seed(42)

# Dimensions
input_dim = 1
hidden_dim = 5
output_dim = 1

# Initialize two linear layers
W1 = torch.randn(input_dim, hidden_dim, requires_grad=True)
b1 = torch.randn(hidden_dim, requires_grad=True)
W2 = torch.randn(hidden_dim, output_dim, requires_grad=True)
b2 = torch.randn(output_dim, requires_grad=True)

# Define predict function (no activation)
def predict(X):
    hidden = X @ W1 + b1
    output = hidden @ W2 + b2
    return output

# Make predictions
y_pred = predict(x)

# Plotting

# Plot predictions vs. true nonlinear data
plt.figure(figsize=(6, 4))
plt.scatter(x.numpy(), y.numpy(), label='True Data', alpha=0.6)
plt.scatter(x.numpy(), y_pred.detach().numpy(), label='Predictions (Linear → Linear)', alpha=0.6)
plt.legend()
plt.title('Prediction with Stacked Linear Layers (No Activation)')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()
