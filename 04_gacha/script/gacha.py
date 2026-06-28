import random
from collections import Counter

def gacha(p):
    n = 0
    while random.random() > p:
        n += 1
    return n

random.seed(0)
N = 100
prob = 0.01
result = [gacha(prob) for _ in range(N)]
hist = Counter(result)

for i in sorted(hist):
    print(i, hist[i])