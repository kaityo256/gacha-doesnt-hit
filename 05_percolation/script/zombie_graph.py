import math
import matplotlib.pyplot as plt

# パラメータ
N = 10000  # 初期人間数
Z0 = 100  # 初期ゾンビ数
r = 1.1  # 感染率
weeks = 30  # 最大週数

humans = N
active_zombies = Z0
cumulative_zombies = Z0

week_list = [0]
human_list = [humans]
zombie_list = [cumulative_zombies]

print("week humans active_zombies cumulative_zombies")

for week in range(weeks + 1):
    print(week, humans, active_zombies, cumulative_zombies)

    new_zombies = math.floor(active_zombies * r)
    new_zombies = min(new_zombies, humans)

    humans -= new_zombies
    active_zombies = new_zombies
    cumulative_zombies += new_zombies

    week_list.append(week + 1)
    human_list.append(humans)
    zombie_list.append(cumulative_zombies)

    if humans == 0 or active_zombies == 0:
        break

# グラフ作成
plt.figure(figsize=(8, 5))

# 下からゾンビ、上に人間
plt.stackplot(
    week_list, zombie_list, human_list, labels=["Cumulative zombies", "Humans"]
)

plt.xlabel("Week")
plt.ylabel("Population")
plt.title(f"Zombie Panic Simulation (r={r})")
plt.legend(loc="upper left")
plt.ylim(0, N + Z0)
plt.grid(True)

filename = f"zombie{int(r*100):02d}.png"
plt.savefig(filename, dpi=300, bbox_inches="tight")
print(f"saved: {filename}")

# plt.show()
