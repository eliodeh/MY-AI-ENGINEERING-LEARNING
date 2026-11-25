For each column k:
  1. PARTIAL PIVOTING: Find the largest |value| in column k at or below row k
     → Swap that row to position k
  2. For each row i below k:
     m = A[i][k] / A[k][k]     (the multiplier)
     Row i ← Row i - m · Row k
