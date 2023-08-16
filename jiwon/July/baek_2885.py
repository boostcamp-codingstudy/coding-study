# https://www.acmicpc.net/problem/2885
# 초콜릿 식사
# 이진변환 후 제곱수 분류를 활용한 문제

import sys

K = int(sys.stdin.readline().strip())       # 6
binK = bin(K)[2:]       # 1 1 0

if binK.count('1') == 1:   # 2의 제곱수이면 나눌 필요는 없음 / 직접 제곱수를 구해서 예외처리하는게 더 빠름
    print(K, 0)
else:       # 아니라면 일단 쪼개고 시작
    choco = 2 ** len(binK)  # 최소한 저 3자리 수보단 큰 초코가 필요
    crop = len(binK)-binK[::-1].find('1')     # 마지막 1이 나올때 까지 쪼개야 다 먹을 수 있음
    print(choco, crop)

'''
    < 더 빠른 방법 : 직접 예외 처리 진행 >
    import sys

    # 우선 2의 제곱수를 모아둠
    stop_number = []
    for i in range(20):
        if 2**i > 1000000:
            break
        stop_number.append(2**i)

    K = int(sys.stdin.readline().strip())       # 6

    if K in stop_number:
        print(K, 0)
    else:
        binK = bin(K)[2:]       # 1 1 0

        choco = 2 ** len(binK)  # 최소한 저 3자리 수보단 큰 초코가 필요
        crop = len(binK)-binK[::-1].find('1')     # 마지막 1이 나올때 까지 쪼개야 다 먹을 수 있음
        print(choco, crop)
'''
