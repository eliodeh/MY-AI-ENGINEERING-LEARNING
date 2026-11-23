def mean(xs): return sum(xs) / len(xs)

def median(xs):
    s = sorted(xs); n = len(s)
    return s[n//2] if n % 2 else (s[n//2 - 1] + s[n//2]) / 2

def mode(xs):
    counts = {}
    for x in xs: counts[x] = counts.get(x, 0) + 1
    return max(counts, key=counts.get)

def variance(xs):          # SAMPLE variance — divide by n-1!
    m = mean(xs)
    return sum((x - m)**2 for x in xs) / (len(xs) - 1)

def std(xs): return math.sqrt(variance(xs))

def percentile(xs, p):     # p in [0,100]
    s = sorted(xs); n = len(s)
    if n == 1: return s[0]
    k = (p / 100) * (n - 1)          # linear interpolation
    lo, hi = math.floor(k), math.ceil(k)
    if lo == hi: return s[int(k)]
    return s[lo] + (k - lo) * (s[hi] - s[lo])

def iqr(xs): return percentile(xs, 75) - percentile(xs, 25)
