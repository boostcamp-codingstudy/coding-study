import sys
import copy

A, B = sys.stdin.readline().split()
A = list(A)
B = list(B)
def cal_diff(n_A,n_B):
    cnt = 0
    for a,b in zip(n_A, n_B):
        if a != b:
            cnt += 1
    return cnt

result = 0
if A in B:
    result = 0
elif len(A) != len(B):
    gap = len(B) - len(A)
    diff_list = []
    for i in range(gap+1):
        new_A = copy.deepcopy(B)
        new_A[i:i+len(A)] = A
        diff = cal_diff(new_A,B)
        diff_list.append(diff)
    result = min(diff_list)
else:
    result = cal_diff(A,B)
    
print(result)