# 付録：プログラムリスト

本書で紹介したシミュレーションを実施するためのプログラムリストです。全てPythonで記述されており、Google ColaboratoryもしくはJupyter Notebookに貼り付けることで実行可能です。

## 2章 リボ払いの恐怖

### 2.1 リボ払いのシミュレーション

```py
import numpy as np
import matplotlib.pyplot as plt

def simulate_revolving_payments(balance, annual_interest_rate, monthly_payment):
    monthly_interest_rate = annual_interest_rate / 12.0
    month = 0
    total = 0
    months = []
    interest_payments = []
    principal_payments = []
    while balance > 0:
        month = month + 1
        interest = int(balance * monthly_interest_rate)
        pay = monthly_payment - interest
        if balance < pay:
            pay = balance
        total += pay
        total += interest
        balance -= pay
        months.append(month)
        interest_payments.append(interest)
        principal_payments.append(pay)
    return months, interest_payments, principal_payments

initial_balance = 790000 # 借入額
annual_interest_rate = 0.15
monthly_payment = 10000
months, interest_payments, principal_payments = simulate_revolving_payments(initial_balance, annual_interest_rate, monthly_payment)
plt.bar(months, interest_payments)
plt.bar(months, principal_payments,bottom=interest_payments)
plt.xlabel("Month")
plt.ylabel("Payment amount")
plt.show()
```

### 2.2 シャーレの中のバクテリア

```py
import matplotlib.pyplot as plt
import numpy as np

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
  x = np.array(x)
  t = 1-1.0/x
  plt.xlabel("Population")
  plt.xlabel("Growth parameter a")
  plt.scatter(x, y, s = 1, label="Simulated data")
  plt.plot(x, t, color = "black", label="Predicted curve")
  plt.legend()

plot(1.0, 3.0)
```

一度実行した後、最後の`plot(1.0, 3.0)`を`plot(3.0, 4.0)`に変えてもう一度実行してみてください。

## 3章　直感はなぜ外れる？

### 3.1 モンティ・ホール問題

キープ派のシミュレーションコード。

```py
from random import choice
games = 10000
wins = 0
for _ in range(games):
    boxes = [1,2,3] # 三つの箱を用意する
    answer = choice(boxes) # 正解の箱を決める
    first_choice = choice(boxes) # 最初の箱を選ぶ
    # 正解と一致していたらアタリ
    if first_choice == answer:
        wins = wins + 1
print(wins/games)
```

チェンジ派のシミュレーションコード。


```py
from random import choice
games = 10000
wins = 0
for _ in range(games):
    boxes = [1,2,3] # 三つの箱を用意する
    answer = choice(boxes) # 正解の箱を決める
    first_choice = choice(boxes) # 最初の箱を選ぶ
    # 最初に選んだ箱がアタリかどうか
    if first_choice == answer: 
        # アタリなら、残りの二つからランダムに選ぶ
        boxes.remove(answer)
        second_choice = choice(boxes)
    else:
        # ハズレなら、残りは必ず正解
        second_choice = answer
    if second_choice == answer:
        wins = wins + 1
print(wins/games)
```

### 3.2 誕生日のパラドックス

```py
import random
from matplotlib import pyplot as plt

def has_shared_birthday(N):
    birthdays = [random.randint(1, 365) for _ in range(N)]
    return len(set(birthdays)) < N

def estimate_probability(N, T):
    count = 0
    for _ in range(T):
        if has_shared_birthday(N):
            count += 1
    return count / T

people = []
probabilities = []

for i in range(10, 40):
    probability = estimate_probability(i, 10000)
    people.append(i)
    probabilities.append(probability)

plt.plot(people, probabilities, marker="o")
plt.xlabel("Number of people")
plt.ylabel("Probability of at least one shared birthday")
plt.ylim(0, 1)
plt.axhline(y=0.5, linestyle="--")
plt.show()
```

## 4章 ガチャの沼へようこそ　

### 4.1 ガチャでレアが外れ続ける「運が悪い」人

以下は「100分の1で当たるガチャを100回引く人が1万人いた時に全て外れる人の数」を計算するコードですが、最初の`n = 100`の箇所を`n = 1000`にすると、「1000分の1で当たるガチャを1000回引く人が1万人いた時に全て外れる人の数」を計算することができます。

```py
import random

N = 10000          # シミュレーションをする人数
n = 100            # 確率は1/n、引く回数もn回
hit_rate = 1 / n
nohit = 0
random.seed(0)
for _ in range(N):
    hit = False

    for _ in range(n):
        if random.random() < hit_rate:
            hit = True

    if not hit:
        nohit += 1

print(f"一度も当たらなかった人 {N}人中{nohit}人")
print(f"一度も当たらなかった人の割合 {nohit / N:.2%}")
```

### 4.2 アイドルのイベント

ポスターをコンプリートするのに平均何枚のCDを購入しなければならないかのシミュレーションコード。

```py
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
```

CDの購入数に対して、「もう一枚CDを購入した時に新しいポスターを獲得できる」確率をプロットするためのコード。

```py
from matplotlib import pyplot as plt

x = []
y = []
for i in range(100):
    x.append(i)
    y.append((43.0/44.0)**i)

plt.xlabel("Number of CDs")
plt.ylabel("Probability of new poster")
plt.plot(x,y, marker='o')
plt.show()
```

