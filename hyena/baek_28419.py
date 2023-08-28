# https://www.acmicpc.net/problem/28419

import sys

n = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().strip().split()))

if n < 3:
    print(-1)
else:    
    evens = 0
    odds = 0
    for i, num in enumerate(nums):
        if i % 2 == 0: # even
            evens += num
        else: # odd
            odds += num

    if evens == odds:
        print(0)
    else:
        if n == 3:
            if odds - evens == 1:
                print(1)
            else:
                print(-1)
        else:
            print(abs(evens-odds))
