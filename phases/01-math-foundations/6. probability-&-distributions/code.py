import random, math
import matplotlib.pyplot as plt

def sample_exponential(lam, n):
    return [-math.log(1 - random.random()) / lam for _ in range(n)]

lam = 1.5
samples = sample_exponential(lam, 10_000)

xs = [i / 100 for i in range(0, 500)]
plt.hist(samples, bins=50, density=True, alpha=0.6)
plt.plot(xs, [lam * math.exp(-lam * x) for x in xs])
plt.show()