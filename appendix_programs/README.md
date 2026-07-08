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
  plt.xlabel("Growth parameter a")
  plt.ylabel("Population")
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

ポスターをコンプリートするのに平均何枚のCDを購入しなければならないかのシミュレーションコードです。

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

CDの購入数に対して、「もう一枚CDを購入した時に新しいポスターを獲得できる」確率をプロットするためのコードです。

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

## 5章 風邪はなぜ流行る？

### 5.1 ゾンビパニック

```py
def zombie(r):
    N = 10000
    z = 100
    N = N - z
    z_total = 0
    weeks = 0
    for i in range(1000):
        weeks += 1
        z_total += z
        z = int(z*r)
        N = N - z
        if N < 0:
            N = 0
        if z == 0 or N == 0:
            break
    return N, weeks

for R in [0.5, 0.9, 1.0, 1.1, 2.0]:
    N, weeks = zombie(R)
    if N >0:
        result = "生存エンド"
    else:
        result = "全滅エンド"
    print(f"R= {R}, 生存者 {N:4d}人, 収束まで {weeks:2d}週, {result}")
```

### 5.2 都市の横断モデル


```py
import random
from matplotlib import pyplot as plt

def find(i, parent):
    while i != parent[i]:
        i = parent[i]
    return i

def union(i, j, parent):
    i = find(i, parent)
    j = find(j, parent)
    parent[j] = i

def make_conf(L, p):
    parent = [i for i in range(L * L)]
    for iy in range(L-1):
        for ix in range(L-1):
            i = ix + iy * L
            j = ix+1 + iy * L
            if random.random() < p:
                union(i, j, parent)
            j = ix + (iy+1) * L
            if random.random() < p:
                union(i, j, parent)
    return parent

def check_percolated(L, p):
    N = L**2
    parent = make_conf(L, p)
    for i in range(L):
        for j in range(N-L-1, N-1):
            if find(i, parent) == find(j, parent):
                return True
    return False

random.seed(1)
trial = 100
L = 32
p_values = []
percolation_probabilities = []
for i in range(100):
    p = i/100.0
    count = 0
    for j in range(trial):
        if check_percolated(L, p):
            count += 1
    P = count / trial
    p_values.append(p)
    percolation_probabilities.append(P)
plt.plot(p_values, percolation_probabilities, marker='o')
plt.xlabel("Probability p")
plt.ylabel("Percolation probability P")
plt.show()
```

## 6章 渋滞はなぜ起きる？

### 6.1 渋滞のシミュレーション

与えられた反射神経パラメータにおいて最適速度模型の時空図を表示するコードです。反射神経パラメータを`a=1.0`とすると渋滞が発生しますが、`a=3.0`とすると渋滞は発生しません。

```py
from math import tanh
from matplotlib import pyplot as plt
import numpy as np

def V(dx):
    return tanh(dx -2.0) + tanh(2.0)

def init(L, number_of_cars, car_positions, car_velocities):
    dx = L / number_of_cars
    x = 0.0
    iv = V(dx)
    for i in range(number_of_cars):
        car_positions[i] = x
        car_velocities[i] = iv
        x += dx
        x += np.random.uniform(-0.5, 0.5)

def step(L, number_of_cars, car_positions, car_velocities, a, dt):
    for i in range(number_of_cars):
        dx = car_positions[(i + 1) % number_of_cars] - car_positions[i]
        if (dx < 0.0):
            dx += L
        car_velocities[i] += a * (V(dx) - car_velocities[i])*dt
        car_positions[i] += car_velocities[i]*dt
        if (car_positions[i] > L):
            car_positions[i] -= L

def run(a):
    T = 50000
    L = 40
    number_of_cars = 20
    dt = 0.002
    car_positions = np.zeros(number_of_cars)
    car_velocities = np.zeros(number_of_cars)
    init(L, number_of_cars, car_positions, car_velocities)
    history = []
    times = []
    data_x = []
    data_y = []
    for i in range(T):
        step(L, number_of_cars, car_positions, car_velocities, a, dt)
        if (i%100==0):
            data_x += car_positions.tolist()
            data_y += [i*dt]*number_of_cars
    plt.xlabel("Position")
    plt.ylabel("Time")
    plt.scatter(data_x, data_y, s=1.0, alpha=0.5,color="black")
    plt.show()

a = 1.0 # 反射神経パラメータ (a=1.0で渋滞相、a=3.0で自由流相)
np.random.seed(1)
run(a)
```

### 6.2 空いている店を選べ！

マイノリティ・ゲームのシミュレーションコードです。何度もゲームを繰り返し、各ターンにおいてプレイヤーが獲得した総得点を表示します。

```py
import numpy as np
import matplotlib.pyplot as plt

def history_to_index(history):
    index = 0
    for bit in history:
        index = 2 * index + bit
    return index

def choose_strategies(strategy_scores, N):
    chosen = []
    for i in range(N):
        max_score = np.max(strategy_scores[i])
        candidates = np.where(strategy_scores[i] == max_score)[0]
        chosen.append(np.random.choice(candidates))
    return chosen

def run_minority_game(N, T, L, S):
    history_length=L
    num_strategies_per_player=S
    num_histories = 2 ** history_length
    strategies = np.random.randint(0, 2,size=(N, num_strategies_per_player, num_histories))
    strategy_scores = np.zeros((N, num_strategies_per_player),dtype=int)
    history = list(np.random.randint(0, 2, size=history_length))
    total_score_per_turn = []
    for t in range(T):
        h_index = history_to_index(history)
        chosen_strategies = choose_strategies(strategy_scores, N)
        choices = np.empty(N, dtype=int)
        for i in range(N):
            s = chosen_strategies[i]
            choices[i] = strategies[i, s, h_index]

        num_A = np.sum(choices == 0)
        num_B = np.sum(choices == 1)
        if num_A < num_B:
            minority_choice = 0
        else:
            minority_choice = 1
        winners = choices == minority_choice
        total_score_per_turn.append(np.sum(winners))
        for i in range(N):
            for s in range(num_strategies_per_player):
                prediction = strategies[i, s, h_index]
                if prediction == minority_choice:
                    strategy_scores[i, s] += 1

        history.pop(0)
        history.append(minority_choice)
    return total_score_per_turn


np.random.seed(1)
N = 101 # プレイヤー数
T = 100 # 総ターン数
L = 5   # 履歴をどれくらい見るか
S = 2   # プレイヤーに配る戦略数 
total_score_per_turn = run_minority_game(N, T, L, S)
# 時間発展をプロット
plt.figure(figsize=(10, 5))
plt.plot(total_score_per_turn)
plt.ylim(bottom=0)
plt.xlabel("Turn")
plt.ylabel("Total score gained in this turn")
plt.title("Total number of winners per turn")
plt.show()
```
