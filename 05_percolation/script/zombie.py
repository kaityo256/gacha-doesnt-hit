import sys

N = 10000
z = 100
N = N - z
r = 0.5
z_total = 0
weeks = 0

r = float(sys.argv[1])

for i in range(1000):
    print(f"{weeks} {z} {z_total} {N}")
    weeks += 1
    z_total += z
    z = int(z*r)
    N = N - z
    if N < 0:
        N = 0
    if z == 0 or N == 0:
        break
print()
print(f"{weeks} weeks later, Z_total = {z_total} N={N}")
