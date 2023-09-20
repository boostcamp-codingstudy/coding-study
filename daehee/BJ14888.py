# # standard solution - time limit exceeded
# from itertools import permutations as P
# *A,=map(int,open(0).read().split())
# n=A[0];N=A[1:n+1];B=['+','-','*','//'];C=[]
# for a,b in zip(A[n+1:],B):C+=a*[b] if a else []
# m,k=-1e9,1e9
# for O in P(C,n-1):
#     t=N[0]
#     for o,n in zip(O,N[1:]):t=eval(f'{t}{o}{n}')if o!='//'else (abs(t)//n*t//abs(t)if t else 0)
#     if t>m:m=t
#     if t<k:k=t
# print(m)
# print(k)

# standard solution 2 - slow
def D(t,j=1):
    global m,k
    if j<n:
        for i in range(4):
            if C[i]:
                C[i]-=1
                D(eval(f'{t}{B[i]}{N[j]}'),j+1)if i<3 else D(((abs(t)//N[j])*(t//abs(t))if t else 0),j+1)
                C[i]+=1
    else:
        if t>m:m=t
        if t<k:k=t
*A,=map(int,open(0).read().split())
n=A[0];N=A[1:n+1];B=['+','-','*','//'];C=A[n+1:];m,k=-1e9,1e9
D(N[0])
print(int(m))
print(int(k))

# # the best solution translated - slower than standard solution
# def D(t,c,j,O):
#     global m,k
#     if j<n-1:
#         for i in range(4):
#             if O[i]:O[i]-=1;D(C(i,t,N[j]),c+(10**i),j+1,O);O[i]+=1
#     else:m,k=max(m,t),min(k,t)
# import sys
# r=sys.stdin.readline
# n=int(r());s,*N=map(int,r().split());*O,=map(int,r().split())
# B=['+','-','*','//'];m,k,f,u=-1e9,1e9,0,1
# C=lambda o,a,b:eval(f'{a}{B[o]}{b}')if o<3 else(abs(a)//b*a//abs(a)if a else 0)
# for i in range(4):f+=O[i]*u;u*=10
# D(s,0,0,O);print(int(m));print(int(k))