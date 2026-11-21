import math

def softmax_naive(logits):
    exps = [math.exp(z) for z in logits]
    total = sum(exps)
    return [e / total for e in exps]

def softmax_stable(logits):
    m = max(logits)
    exps = [math.exp(z - m) for z in logits]
    total = sum(exps)
    return [e / total for e in exps]

# Test with safe logits
print(softmax_naive([2.0, 1.0, 0.1]))   # works
print(softmax_stable([2.0, 1.0, 0.1]))  # same result

# Test with dangerous logits
print(softmax_stable([100.0, 101.0, 102.0]))  # [0.090, 0.245, 0.665]
# softmax_naive([100, 101, 102]) → [nan, nan, nan] because exp(100) = inf