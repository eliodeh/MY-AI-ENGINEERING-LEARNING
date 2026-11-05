This lesson teaches you how computers calculate gradients (derivatives) automatically, especially when training neural networks.
1. What is a derivative?
A derivative tells us how much a value changes when another value changes.

In machine learning, derivatives help us understand how changing a model's weights affects its error (loss).
2. What is the Chain Rule?
The chain rule helps us calculate the derivative of a function that depends on other functions.

It is important because neural networks contain many connected operations.
3. What is Automatic Differentiation?
Automatic differentiation (Autodiff) is a technique that automatically calculates derivatives by tracking mathematical operations.

It uses two main steps:
- Forward pass: Calculates the output of each operation.
- Backward pass: Calculates gradients by working backwards through the operations.
4. What is Backpropagation?
Backpropagation uses the chain rule to calculate how much each weight contributes to the model's error.

The gradients help the model adjust its weights and improve its predictions.
5. What will you build?
You will build a small automatic differentiation engine in Python using a Value class.

You will then use it to:
- Perform mathematical operations.
- Calculate gradients.
- Build a simple neural network.
- Train the network using gradient descent.
- Check your gradients against numerical calculations and PyTorch.
6. Why is this important in AI?
Autodiff is one of the foundations of deep learning. Libraries such as PyTorch use automatic differentiation to calculate gradients when training neural networks, including large language models.

Automatic differentiation allows a computer to calculate how each input or weight affects the final result. These calculations help neural networks learn by adjusting their weights to reduce errors.