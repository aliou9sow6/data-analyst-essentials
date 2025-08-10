import torch

# Mean Squared Error (MSE) function
def mse_loss(predictions, targets):
    return torch.mean((predictions - targets) ** 2)

# Example: ground truth vs. predictions
Y_true = torch.tensor([[2.0], [4.0], [6.0], [8.0]])      # True targets
Y_pred = torch.tensor([[2.5], [3.5], [5.5], [8.5]])      # Model predictions

# Compute loss
loss = mse_loss(Y_pred, Y_true)
print("MSE Loss:", loss.item()) 

W = torch.randn((8, 1), requires_grad=True)
b = torch.zeros((1,), requires_grad=True)

print("W : \n", W)
print("\nb : ", b)
