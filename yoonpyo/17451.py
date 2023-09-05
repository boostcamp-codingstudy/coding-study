import sys
n=int(sys.stdin.readline())
V=list(map(int,sys.stdin.readline().split()))
answer=V[n-1]
for i in range(n-1,0,-1):
    if answer<=V[i-1]:
        answer=V[i-1]
    else:
        if V[i]%V[i-1]==0:
            answer=(V[i]//V[i-1])*V[i-1]
        else:
            answer=(V[i]//V[i-1]+1)*V[i-1]
        V[i-1]=answer
print(V[0])