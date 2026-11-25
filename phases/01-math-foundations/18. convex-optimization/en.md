# Convex Problems
Convex problems have one valley so gradient descent is guaranteed to reach the global minimum (testable via f''≥0 or a positive-semidefinite Hessian, and solvable faster with Newton's method using the inverse Hessian), while neural networks are non-convex yet SGD still works because high-dimensional landscapes are mostly escapable saddle points, overparameterization smooths them, and noise finds generalizing flat minima.

# the three areas to look up:
1. Convexity = one valley = guarantees. Test it with f''≥0 or Hessian positive semidefinite.

2. Newton's uses curvature (H⁻¹) instead of a learning rate — quadratic convergence, but O(n³) cost, so only for small convex problems.

3. Deep learning violates convexity but survives because high-dimensional landscapes are mostly saddles (escapable), overparameterization smooths things, and SGD noise finds flat (generalizing) minima.

