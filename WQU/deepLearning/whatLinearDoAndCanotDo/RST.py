import torch

# Define ReLU manually
def my_relu(x):
    return torch.clamp(x, min=0)

# Test on a sample tensor
test_x = torch.tensor([-2.0, -1.0, 0.0, 1.0, 2.0])
print("Input:", test_x)
print("ReLU Output:", my_relu(test_x))

print("#############")

# Define Sigmoid manually
def my_sigmoid(x):
    return 1 / (1 + torch.exp(-x))

# Test
test_x = torch.tensor([-2.0, -1.0, 0.0, 1.0, 2.0])
print("Input:", test_x)
print("Sigmoid Output:", my_sigmoid(test_x))

print("#############")

# Step 1: Define the tanh function manually
def my_tanh(x):
    return (torch.exp(x) - torch.exp(-x)) / (torch.exp(x) + torch.exp(-x))

# Step 2: Test input
test_x = torch.tensor([[-2.0, -1.0, 0.0, 1.0, 2.0]])

# Step 3: Print results
print("Input:", test_x)
print("Tanh Output:", my_tanh(test_x))