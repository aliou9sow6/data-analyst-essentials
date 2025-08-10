import torch

from noise import x
# Set seed
torch.manual_seed(0)

# Input tensor (4 samples, 1 feature)
x = torch.tensor([[1.0], [2.0], [3.0], [4.0]])

# Define dimensions
input_dim = 1
hidden_dim = 3
output_dim = 1

# Initialize parameters
W1 = torch.randn(1, 3, requires_grad=True)
b1 = torch.randn(3, requires_grad=True)
W2 = torch.randn(3, 1, requires_grad=True)
b2 = torch.randn(1, requires_grad=True)

# Define forward function
def predict(X):
    hidden = X @ W1 + b1
    output = hidden @ W2 + b2
    return output

# Compute prediction
y_pred = predict(x)
print("y_pred:", y_pred)