import torch
import pandas as pd
from sklearn.preprocessing import StandardScaler

# 1. Load dataset
data = pd.read_csv("Concrete_Data.csv")  # Adjust path as needed

# 2. Separate features and target
inputs = data.iloc[:, :-1].values       # First 8 columns = features
targets = data.iloc[:, -1].values.reshape(-1, 1)  # Last column = target

# 3. Normalize input features
scaler = StandardScaler()
inputs_scaled = scaler.fit_transform(inputs)

# 4. Convert to PyTorch tensors
inputs_tensor = torch.tensor(inputs_scaled, dtype=torch.float32)
targets_tensor = torch.tensor(targets, dtype=torch.float32)

# 5. Shuffle and split into training (80%) and test (20%) sets
torch.manual_seed(42)
n_samples = inputs_tensor.shape[0]
indices = torch.randperm(n_samples)
split_idx = int(n_samples * 0.8)

train_indices = indices[:split_idx]
test_indices = indices[split_idx:]

X_train = inputs_tensor[train_indices]
y_train = targets_tensor[train_indices]
X_test = inputs_tensor[test_indices]
y_test = targets_tensor[test_indices]

# 6. Initialize model parameters
num_features = X_train.shape[1]  # Should be 8
W = torch.randn((num_features, 1), requires_grad=True)
W.data *= 0.01  # Scale down initial values
b = torch.zeros((1,), requires_grad=True)

# 7. Confirm everything is set up
print("Training set size:", X_train.shape[0])
print("Test set size:", X_test.shape[0])
print("Weight shape:", W.shape)
print("Bias shape:", b.shape)