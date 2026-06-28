import random

N = 10000          # シミュレーションをする人数
n = 1000            # 確率は1/n、引く回数もn回
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