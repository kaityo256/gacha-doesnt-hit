import random
import numpy as np

def calc_any():
  cd = np.zeros(44)
  n = 0
  while np.any(cd == 0):
    i = random.randint(0,43)
    cd[i] = 1
    n += 1
  return n

def calc_np():
  cd = np.zeros(44)
  n = 0
  while np.prod(cd) == 0:
    i = random.randint(0,43)
    cd[i] = 1
    n += 1
  return n

def calc_num():
  cd = []
  n = 0
  while len(set(cd)) < 44:
    i = random.randint(1,44)
    cd.append(i)
    #cd = list(set(cd))
    n += 1
  return n

def calc_bit():
  seen = 0
  all_seen = (1 << 44) - 1

  count = 0

  while seen != all_seen:
      x = random.randrange(44)
      seen |= 1 << x
      count += 1
  return count

if __name__ == '__main__':
  n = 10000
  total = 0
  for i in range(n):
    # total += calc_num() # 5.69
    # total += calc_any() # 14.619
    # total += calc_np() # 9.156
    total += calc_bit() # 1.217
  print(total/n)