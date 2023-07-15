import sys

input = sys.stdin.readline
s, p = map(int, input().split())
dna = list(input())
a, c, g, t = map(int, input().split())


def sol(cntlst):
    if (cntlst[0] >= a) and (cntlst[1] >= c) and (cntlst[2] >= g) and (cntlst[3] >= t):
        return True
    else:
        return False


tmp = dna[:p]
dp = [[] for i in range(s - p + 1)]
dp[0] = [tmp.count("A"), tmp.count("C"), tmp.count("G"), tmp.count("T")]
for i in range(1, s - p + 1):
    A, C, G, T = 0, 0, 0, 0
    if dna[p - 1 + i] == "A":
        A += 1
    elif dna[p - 1 + i] == "C":
        C += 1
    elif dna[p - 1 + i] == "G":
        G += 1
    elif dna[p - 1 + i] == "T":
        T += 1
    if dna[i - 1] == "A":
        A -= 1
    elif dna[i - 1] == "C":
        C -= 1
    elif dna[i - 1] == "G":
        G -= 1
    elif dna[i - 1] == "T":
        T -= 1
    dp[i] = [dp[i - 1][0] + A, dp[i - 1][1] + C, dp[i - 1][2] + G, dp[i - 1][3] + T]
cnt = 0
# print(dp)
for i in dp:
    if sol(i):
        cnt += 1

print(cnt)
