# standard solution - passed using PyPy3
#                   - time limit exceeded using Python3
R=open(0).readline
r,c,h=map(int,R().split())
M=[[[0]*c for j in range(r)] for i in range(h)]
C=[[[0]*c for j in range(r)] for i in range(h)]
D=[]
for i in range(-1,2):
    for j in range(-1,2):
        for k in range(-1,2):D+=[[i,j,k]]if(i,j,k)!=(0,0,0)else[]
for i in range(h):
    for j in range(r):
        for k,e in enumerate(R().rstrip()):
            if e=='*':M[i][j][k]=1
for i in range(h):
    for j in range(r):
        for k in range(c):
            for d in D:
                u,v,w=i+d[0],j+d[1],k+d[2]
                if -1<u<h and -1<v<r and -1<w<c:C[i][j][k]+=M[u][v][w]
for i in range(h):
    for j in range(r):
        for k in range(c):
            print('*'if M[i][j][k]else C[i][j][k]%10,end='')
        print()