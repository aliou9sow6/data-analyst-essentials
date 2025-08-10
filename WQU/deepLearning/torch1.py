import torch

# Scalar: 0D tensor
my_scalar = torch.tensor(10)
print("Scalar:", my_scalar) 
print("Shape:", my_scalar.shape)

# Vector: 1D tensor
my_vector = torch.tensor([5, 10, 15])
print("\nVector:", my_vector)
print("Shape:", my_vector.shape)

# Matrix: 2D tensor
my_matrix = torch.tensor([[1, 2, 3], [10, 20, 30]])
print("\nMatrix:", my_matrix)
print("Shape:", my_matrix.shape)

# 3D Tensor
tensor_3d = torch.randn(2, 3, 4)  # random numbers
print("\n3D Tensor:", tensor_3d)
print("Shape:", tensor_3d.shape)

# Information about my tensors
print(".dtype : ", tensor_3d.dtype)
print(".device : ", my_matrix.device) 
