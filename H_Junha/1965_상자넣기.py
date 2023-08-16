import sys

N = int(sys.stdin.readline())
BOXES = list(map(int,sys.stdin.readline().split()))

dp = [1]*N

for idx in range(N):
    prev_box = BOXES[:idx]
    results = []
    for i,p in enumerate(prev_box):
        if p < BOXES[idx]:
            results.append(dp[i])
    if results:
        dp[idx] += max(results)
print(max(dp))