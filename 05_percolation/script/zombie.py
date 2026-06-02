import sys

N = 10000
z = 100
N = N - z
r = 0.5
z_total = 0
weeks = 0

r = float(sys.argv[1])

for i in range(1000):
    weeks += 1
    z_total += z
    N = N - z
    if N < 0:
        N = 0
    print(f"{i+1} {z} {z_total} {N}")
    z = int(z*r)
    if z == 0 or N == 0:
        break
print()
print(f"{weeks} weeks later, N={N}")
