from itertools import combinations
N,M = list(map(int,input().split())) #전체 아이스크림 개수 # 섞어먹으면 안되는 조합 수

possible = list(combinations([i+1 for i in range(N)],3))
ori_possible = possible[:]

ice = [[False for i in range(N)] for j in range(N)]
result = 0
# 1,2,3,4,5
remove_list = []
for test_case in range(M):
    comb = list(map(int, input().split()))
    ice[comb[0]-1][comb[1]-1] = True
    ice[comb[1]-1][comb[0]-1] = True

for p in possible:
    if ice[p[0]-1][p[1]-1] or ice[p[0]-1][p[2]-1] or ice[p[1]-1][p[2]-1]:
        result+= 1 
       

print(len(possible) - result)

    
    
        



