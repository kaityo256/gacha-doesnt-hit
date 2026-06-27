import matplotlib.pyplot as plt

def logistic_plot(start, end, x, y):
  for i in range(1000):
    r = (end - start) * i / 1000 + start
    n = 0.1
    for j in range(1000):
      n = r * n * (1.0 - n)
      if j > 900:
        x.append(r)
        y.append(n)

def plot(start, end):
  x, y = [], []
  logistic_plot(start, end, x, y)
  plt.scatter(x, y, s = 0.1)

plot(1.0, 3.0)
