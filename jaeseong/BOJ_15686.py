import sys
sys.stdin = open('input.txt')


n,m = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(n)]


def length(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

# 도시의 치킨거리 = 모든 집의 치킨거리의 합
# 치킨거리는 집부터 가장 가까운 치킨집 사이의 거리
# 도시의 치킨거리가 최소가 되도록 하는 m개의 자리를 고르기 
# -> 모든 치킨자리에서 m개의 조합수에서 각 집마다 거리가 최소로 되도록(시간초과?)

chickens = []
houses = []
for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i][j] == 2:
            chickens.append((i,j))
        elif arr[i][j] == 1:
            houses.append((i,j))


from itertools import combinations

answer = 1e9 # 도시의 치킨거리

for chicken in combinations(chickens,m):

    # 모든 집에서 최소거리 구하기
    total = 0
    for house in houses: #각 집마다 가장 가까운 치킨집을 찾고 더하기
        distance = 1e9
        for c in chicken:
            distance = min(length(house,c),distance) 
        # 각 집에서 가장 가까운 치킨집을 구하면 answer에 더함
        total += distance
    answer = min(total,answer)

print(answer)


