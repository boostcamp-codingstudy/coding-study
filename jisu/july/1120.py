import sys

input = sys.stdin.readline
X, Y = map(str, input().split())
K = len(Y) - len(X)
diflst = []
for i in range(K + 1):
    st = i
    dif = 0
    for j in range(len(X)):
        if X[j] != Y[j + i]:
            dif += 1
    diflst.append(dif)
# print(diflst)
print(min(diflst))
