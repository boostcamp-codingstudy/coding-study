# # standard solution
# *A,=map(int,open(0).read().split())
# n=A[0];A=A[1:];C=[0]*3
# for i in range(n):
#     T=[0]*3
#     for j in range(3):T[j]=A[3*i+j]+min(C[:j]+C[j+1:])
#     C=T
# print(min(C))

# standard solution 2
import sys
input=sys.stdin.readline
n=int(input());C=[0]*3
for i in range(n):
    T=[0]*3
    for j,a in enumerate(map(int,input().split())):T[j]=a+min(C[:j]+C[j+1:])
    C=T
print(min(C))