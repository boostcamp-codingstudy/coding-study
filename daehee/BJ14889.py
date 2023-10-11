# # standard solution using combination - very slow
# from itertools import combinations as C
# *A,=map(int,open(0).read().split())
# n=A[0];A=A[1:];s=sum(A);B=[];h=n//2
# S=set(range(n))
# for c in C(range(n),h):
#     b,d=0,0
#     D=S-set(c)
#     for i in c:
#         for j in c:b+=A[i*n+j]
#     for i in D:
#         for j in D:d+=A[i*n+j]
#     B+=[abs(b-d)]
# print(min(B))

# standard solution using backtracking
*A,=map(int,open(0).read().split())
n=A[0];A=A[1:];d=40000;h=n//2
def F(B,C,b,c,i):
    global d
    if d:
        if len(B)<h:
            for j in range(i+1,n):
                a,s=0,0
                for k in B:a+=A[k*n+j]+A[j*n+k]
                for k in C:s+=A[k*n+j]+A[j*n+k]
                F(B+[j],C-{j},b+a,c-s,j)
        else:
            t=abs(b-c)
            if t<d:d=t
    else:return
F([],set(range(n)),0,sum(A),0)
print(d)