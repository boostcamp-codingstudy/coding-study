# standard solution
*A,=map(int,open(0).read().split())
A=A[1:];K='AxBCxDxEFxGx'
for i,k in enumerate(K):
    if k=='x':continue
    j,f=i,1
    for a in A:
        j=(j+a)%len(K)
        if K[j]=='x':f=0;break
    if f:print(k,K[j])

# # standard solution 2 - interestingly, it is bit slower and bit longer
# *A,=map(int,open(0).read().split())
# A,K=A[1:],'AxBCxDxEFxGx'
# for i,k in enumerate(K):
#     if k!='x':
#         j,f=i,1
#         for a in A:
#             j=(j+a)%len(K)
#             if K[j]=='x':f=0;break
#         if f:print(k,K[j])