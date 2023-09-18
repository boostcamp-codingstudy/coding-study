# # standard solution
# *A,=map(int,open(0).read().split())
# print(*sorted(A[1:]),sep='\n')

# the best solution
i=iter(open(0));next(i)
print(*sorted(map(int,i)),sep='\n')