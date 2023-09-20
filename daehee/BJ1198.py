from itertools import combinations as C
*A,=map(int,open(0).read().split())
n=A[0];A=A[1:];P=[];S=[]
for i in range(n):P+=[A[2*i:2*i+2]]
for T in C(P,3):
    t=[]
    for i in range(3):t+=[((T[i-1][0]-T[i][0])**2+(T[i-1][1]-T[i][1])**2)**.5]
    s=sum(t)/2;s=(s*(s-t[0])*(s-t[1])*(s-t[2]));S+=[s]
print(max(S)**.5)