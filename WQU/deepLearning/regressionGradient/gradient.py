# Set learning rate and number of training epochs
learning_rate = 0.001
epochs = 100

# Training loop
for epoch in range(epochs):
    # 1. Forward pass: compute predictions
    y_pred = predict(X_train)
    
    # 2. Compute loss
    loss = mse_loss(y_pred, y_train)
    
    # 3. Backward pass: compute gradients
    loss.backward()

    # 4. Update parameters
    with torch.no_grad():
        W -= learning_rate * W.grad
        b -= learning_rate * b.grad

    # 5. Zero gradients
    W.grad.zero_()
    b.grad.zero_()

    # Print loss every 10 epochs
    if (epoch + 1) % 10 == 0:
        print(f"Epoch {epoch+1}: Loss = {loss.item():.4f}")
