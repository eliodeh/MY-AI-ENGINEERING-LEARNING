# Linear systems
Every ML problem that involves fitting parameters is a linear system — and the method you choose (Gaussian elimination, LU, QR, Cholesky, SVD, or CG) depends on the structure of your matrix and how many times you need to solve it.


# Machine Learning Connections:
1. Linear regression = solving normal equations XᵀXw = Xᵀy

2. Ridge regression = solving (XᵀX + λI)w = Xᵀy via Cholesky

3. Gaussian processes = Cholesky factorization of the kernel matrix K

4. Orthogonal initialization = QR decomposition of weight matrices

5. Preconditioning = incomplete LU/Cholesky for conjugate gradient

# The Problem
Solve Ax = b — find the unknown vector x given matrix A and output b. In ML, this is linear regression, least squares, Gaussian processes, and neural network layers.


