# https://www.acmicpc.net/problem/1244
# 스위치 켜고 끄기
# 단순 문제해결 문제, 나머지 연산 / range 활용


import sys

students = int(sys.stdin.readline())
lights = [0]+list(map(int, sys.stdin.readline().split()))
N = int(sys.stdin.readline())

for _ in range(N):
    stype, pos = map(int, sys.stdin.readline().split())
    if stype == 1:        # 남자
        for idx in range(int(pos), len(lights), int(pos)):
            lights[idx] = (lights[idx]+1) % 2
    else:       # 여자
        i = 0
        while 1 <= pos-i and pos + i <= len(lights)-1 and lights[pos-i] == lights[pos+i]:
            lights[pos-i], lights[pos +
                                  i] = (lights[pos-i]+1) % 2, (lights[pos+i]+1) % 2
            i += 1

for i in range(1, students+1):
    print(lights[i], end=" ")
    if not i % 20:
        print()
