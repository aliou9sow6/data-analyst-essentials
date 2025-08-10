import torch
import matplotlib.pyplot as plt

# Generate input values
x = torch.linspace(0, 2, 100).unsqueeze(1)

# Create nonlinear targets: y = x^2 + small noise
y = x**2 + 0.1 * torch.randn_like(x)

# Plot the data
plt.figure(figsize=(6, 4)) 
plt.scatter(x.numpy(), y.numpy(), alpha=0.7)
plt.title('Nonlinear Pattern: $y = x^2 + \\epsilon$')  # Or: 'y = x² + noise'
plt.xlabel('Input $x$')
plt.ylabel('Target $y$')
plt.grid(True)
plt.show()
