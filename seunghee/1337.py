import sys
from math import inf
n = int(sys.stdin.readline().strip())
data = [int(sys.stdin.readline().strip()) for _ in range(n)]
data.sort()
ans = inf

start = 0
end = 0
while True:
    if start == n:
        break

    if end < n and data[end] <= data[start]+4: # 시작 숫자를 기준으로 비교 숫자가 시작+4안에 있는지 계속 확인
        end += 1
    else:# 시작과 끝을 정하구 그 사이에 필요한 숫자가 몇개인지 확인
        ans = min(ans, len(set([x for x in range(data[start], data[start]+ 5)]) - set(data[start:end+1])))
        # 시작 숫자를 바꿈
        start +=1
        end = start
print(ans)
