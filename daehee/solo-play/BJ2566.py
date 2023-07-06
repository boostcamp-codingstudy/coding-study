# my solution
# M,I,J=-1,-1,-1
# for i in range(9):
#     for j,e in enumerate(map(int,input().split())):
#         if e>M:M,I,J=e,i,j
# print(M);print(I+1,J+1)

# the best solution by ljwljw8541
a=*map(int,open(0).read().split()),
i=a.index(M:=max(a))
print(M);print(i//9+1,i%9+1)