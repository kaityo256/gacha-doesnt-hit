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
