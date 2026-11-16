import math

def information_content(p, base=2):
    if p <= 0:
        return float("inf")
    if p > 1:
        return 0.0
    return -math.log(p) / math.log(base)

def entropy(probs, base=2):
    return sum(
        p * information_content(p, base)
        for p in probs if p > 0
    )
fair_coin = [0.5, 0.5]
biased_coin = [0.99, 0.01]

print(entropy(fair_coin))
print(entropy(biased_coin))