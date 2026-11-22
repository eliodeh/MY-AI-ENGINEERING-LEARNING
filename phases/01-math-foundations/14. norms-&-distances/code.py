import math
import numpy as np

# --- Norms ---
def l1_norm(x):
    return sum(abs(xi) for xi in x)

def l2_norm(x):
    return math.sqrt(sum(xi**2 for xi in x))

def lp_norm(x, p):
    return sum(abs(xi)**p for xi in x) ** (1/p)

def linf_norm(x):
    return max(abs(xi) for xi in x)

# --- Distances between two vectors ---
def l1_distance(a, b):
    return sum(abs(ai - bi) for ai, bi in zip(a, b))

def l2_distance(a, b):
    return math.sqrt(sum((ai - bi)**2 for ai, bi in zip(a, b)))

def linf_distance(a, b):
    return max(abs(ai - bi) for ai, bi in zip(a, b))

def cosine_similarity(a, b):
    dot = sum(ai * bi for ai, bi in zip(a, b))
    norm_a = l2_norm(a)
    norm_b = l2_norm(b)
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)

def cosine_distance(a, b):
    return 1 - cosine_similarity(a, b)

def dot_product(a, b):
    return sum(ai * bi for ai, bi in zip(a, b))

def mahalanobis_distance(x, y, cov_matrix):
    diff = np.array(x) - np.array(y)
    inv_cov = np.linalg.inv(cov_matrix)
    return math.sqrt(diff.T @ inv_cov @ diff)

# --- Set-based ---
def jaccard_similarity(set_a, set_b):
    intersection = len(set_a & set_b)
    union = len(set_a | set_b)
    if union == 0:
        return 1.0
    return intersection / union

def jaccard_distance(set_a, set_b):
    return 1 - jaccard_similarity(set_a, set_b)

