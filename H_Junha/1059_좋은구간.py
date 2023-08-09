import sys

L = int(sys.stdin.readline())
NUM = list(map(int,sys.stdin.readline().split()))
N = int(sys.stdin.readline())

NUM.sort()

s = 0
e = L-1

if N in NUM:
    print(0)
else:
    if NUM[0] > N:
        rng = [i for i in range(1,NUM[0])]
    else:
        while True:
            if NUM[s] < N :
                s += 1
            if NUM[e] > N:
                e -= 1
            if NUM[s] > N and NUM[e] < N:
                break
        rng = [i for i in range(NUM[s-1]+1,NUM[e+1],1)]

    answer = []

    for i in range(0, rng.index(N)+1, 1):
        for j in range(len(rng)-1,rng.index(N)-1,-1):
            if not(i==j):
                answer.append([rng[i],rng[j]])
    print(len(answer))