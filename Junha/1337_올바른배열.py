import sys

# 계단식으로 5개의 수가 정렬되면 올바른 배열

N = int(sys.stdin.readline()) #배열의 크기

ARR = []

for n in range(N):
    ARR.append(int(sys.stdin.readline()))

ARR.sort()

result = []
for i in ARR:
    new_arr = [j for j in range(i,i+5)]
    result.append(len(set(new_arr) - set(ARR)))
print(min(result))

    
