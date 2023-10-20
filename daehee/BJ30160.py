# standard solution - time limit exceeded
# *A,=map(int,open(0).read().split())
# n=A[0];A=A[1:];s=0
# for k in range(1,n+1):
#     for i in range(k):s+=(2*k-2*i-1)*A[i]
#     print(s,end=' ')

# standard solution 2
*A,=map(int,open(0).read().split())
n=A[0];A=A[1:];B=[A[0]]
for i in range(1,n):B+=[B[i-1]+A[i-1]+A[i]]
for _ in range(2):
    for i in range(1,n):B[i]+=B[i-1]
print(*B,sep=' ')

# # the best solution
# a=b=c=0
# for i in open(0).read().split()[1:]:i=int(i);a+=i;b+=a*2-i;c+=b;print(c,end=' ')