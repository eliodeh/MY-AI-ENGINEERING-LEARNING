import random, math

def sample_exponential(lam):
    u = random.random()          # uniform in [0,1)
    return -math.log(u) / lam    # inverse CDF of exponential

samples = [sample_exponential(1.0) for _ in range(10000)]
print(sum(samples)/len(samples))  # should be ≈ 1.0 (mean = 1/λ)