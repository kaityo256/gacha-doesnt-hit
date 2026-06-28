import random

total = 0
for i in range(10000):
  cd = []
  n = 0
  while len(set(cd)) < 44:
    i = random.randint(1,44)
    cd.append(i)
    n += 1
  total += n

print(total/10000)