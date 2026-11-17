np.random.seed(42)
A = np.random.randn(5, 4)
U, S, V = svd_from_scratch(A)
U_np, S_np, Vt_np = np.linalg.svd(A, full_matrices=False)

print("Ours:  ", np.round(S, 4))
print("NumPy: ", np.round(S_np, 4))
print("Error:", np.linalg.norm(A - U @ np.diag(S) @ V.T))