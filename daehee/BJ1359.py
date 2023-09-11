# # standard solution
# n,m,k=map(int,input().split())
# def C(a,b):
#     n,d=1,1
#     for i in range(b):n*=(a-i);d*=(i+1)
#     return n//d
# c,s=C(n,m),0
# while m>=k:
#     if n+k<m+m:k+=1;continue
#     p=C(m,k)*C(n-m,m-k);s+=p/c;k+=1
# print(s)

# # standard solution using itertools.combinations
# from itertools import combinations as C
# n,m,k=map(int,input().split())
# A,s=[*C(range(n),m)],0
# for I in A:
#     for J in A:s+=len(set(I)&set(J))>=k
# print(s/len(A)**2)

# the best solution 
from itertools import combinations as C
n,m,k=map(int,input().split())
A=[*C(range(n),m)];s=0
for I in A:
    c=0
    for j in range(m):c+=I[j]<m
    s+=c>=k
print(s/len(A))