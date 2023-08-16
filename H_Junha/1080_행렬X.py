import sys

N, M = map(int, sys.stdin.readline().split())

A = [list(map(int, sys.stdin.readline().strip())) for i in range(N)]
B = [list(map(int, sys.stdin.readline().strip())) for i in range(N)]

NEW = []
for a,b in zip(A, B):
    temp = []
    for i,j in zip(a,b):
        temp.append(int(i) ^ int(j))
    NEW.append(temp)
    
if N%3 == 0 and M%3 == 0:
    for row in NEW:
        

# print(1 and 1)
# for i in A:
#     print(i)
# print()
# for i in B:
#     print(i)
    
#[0, 0, 1]
# [1, 0, 0]
# [1, 0, 0]
# [0, 0, 0]
# [0, 1, 1]
# [0, 1, 0]
# [1, 0, 0]
# [1, 0, 0]
# [0, 1, 0]
# [0, 1, 0]
# [0, 1, 0]
# [1, 1, 0]
# [1, 0, 1]
# [1, 0, 1]
# [0, 0, 0]
# [1, 1, 0]
# [0, 0, 0]
# [1, 1, 0]

# [0, 0, 1]
# [1, 0, 0]
# [0, 1, 1]
# [0, 0, 0]
# [1, 0, 0]
# [0, 1, 0]
# [0, 1, 1]
# [1, 0, 0]
# [1, 0, 1]
# [1, 0, 1]
# [0, 1, 0]
# [0, 0, 1]
# [0, 1, 0]
# [0, 1, 0]
# [1, 1, 1]
# [1, 1, 0]
# [1, 1, 1]
# [0, 0, 1]