'''
계단의 개수는 순차적으로 아래와 같은 경우로 묶이게 된다. (밟으면 1, 건너뛰면 0)
[0, 1] → [0]
       → [1]
[1, 0] → [1]
[1, 1] → [0]
따라서, 현재 단계가 밟히기 위해서는 아래와 같은 경우가 선행 되어야 한다.
[1, 0, 1]
[1, 1, 0]
[0, 1, 0]
선행 경우의 수 중 가장 높은 점수를 골라 현재 단계에 누적 한다.
'''
def solution():
    n = int(input())
    stair = []
    point = [0] * n
    for _ in range(n):
        stair.append(int(input()))
    point[0] = stair[0]
    if n > 1: point[1] = stair[0] + stair[1]
    if n > 2: point[2] = max(stair[0], stair[1]) + stair[2]
    if n > 3:
        for i in range(3, n):
            point[i] = max(point[i - 3] + stair[i - 1], point[i - 2]) + stair[i]
    print(point[-1])
    
solution()