import sys
N, M = map(int, sys.stdin.readline().strip().split(' '))
A = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
B = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]


cnt = 0
print(A)

# print(sum(A-B))
# if N <= 3 and M <= 3: 
#     if  A == B or sum(A-B) == 0 or sum(B-A) == 0:
        
#     else:
#         return -1

# else:
#     if 
    
#     difference = [[True for _ in range(M)] for _ in range(N)] # 다르면 False
#     for i in range(N):
#         for j in range(M):
#             if A[i][j] != B[i][j]:
#                 difference[i][j] = False

#     꼭지점 쪽 좌우, 위아래는 서로 같아야됌 :
    
#     else:
#         return -1

# print(difference)
# print(sum(difference))
# print(all(difference))


# # [[True, True, True],
# # [True, True, True],
# # [False, False, False],
# # [True, True, True],
# # [False, False, False],
# # [True, True, True], 
# # [False, False, False], 
# # [True, True, True], 
# # [False, False, False],
# # [False, False, False],
# # [True, True, True],
# # [False, False, False],
# # [False, False, False],
# # [False, False, False],
# # [False, False, False],
# # [True, True, True],
# # [False, False, False],
# # [False, False, False]]
# # # for i in range(M-N+1):
# #     reverse_A = 

# # 0000 1001
# # 0010 1011
# # 0000 1001
# # 변경이 필요한 부분 FAlse
# # FTTF
# # FTTF
# # FTTF

# # 1221
# # 1221
# # 1221

# # 1110
# # 1110
# # 1110
# # 1110

# # 1221
# # 1221
# # 1221


# # 111
# # 111
# # 111


# # 1
# # 0


