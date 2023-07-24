import sys
from collections import deque

def check(bingo):
    cnt = 0
   
    for i in range(5):
        col = 1
        row = 1
        for j in range(5):
            col *= int(bingo[j][i])
            row *= int(bingo[i][j])
        if col != 0:
            cnt += 1
        if row != 0:
            cnt += 1
    
    diag_1 = 1
    diag_2 = 1
    for i,j in zip([0,1,2,3,4], [4,3,2,1,0]): 
        diag_1 *= int(bingo[i][i])
        diag_2 *= int(bingo[i][j])
    if diag_1 != 0:
        cnt += 1
    if diag_2 != 0:
        cnt += 1
        
    return cnt

A = [sys.stdin.readline().strip().split() for i in range(5)]
B = [sys.stdin.readline().strip() for i in range(5)]
B = deque(" ".join(B).split())

new_bingo = [[0 for i in range(5)] for j in range(5)]
count = 0

while True:
    num = B.popleft()
    for i in range(5):
        for j in range(5):
            if num == A[i][j]:
                new_bingo[i][j] = A[i][j]
    count += 1
    if check(new_bingo) >= 3:
        break
print(count)
# print(check(new_bingo))
# for n in new_bingo:
#     print(n)