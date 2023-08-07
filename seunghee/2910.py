import sys
from collections import Counter
N, C = map(int, sys.stdin.readline().strip().split(' '))
nums = [x for x in map(int, sys.stdin.readline().strip().split(' '))]

point = Counter(nums)# most_common() -> 순서 유지 해줌
for num, cnt in point.items():
    order = nums.index(num)
    point[num] = (cnt, order)

ans = []
result = sorted(point.items(), key = lambda item : (-item[1][0], item[1][1]))
for num, info in result:
    ans.extend([num for _ in range(info[0])])
# print(' '.join(map(str, ans)))
print(*ans)

# 64ms

