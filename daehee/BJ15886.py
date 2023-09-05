# *A,=open(0).read().split()
# n,A=int(A[0]),A[1]#;B=[0]*n
# # for i in range(n):
# #     j=i;B[j]+=1
# #     print(j)
# #     for _ in range(n-1):
# #         print(A[j],j,end='->')
# #         if A[j]=='E':j+=1
# #         else:j-=1
# #         print(j)
# #         B[j]+=1
# #     print(B)
# f,c=0,0
# for a in A:
#     if a=='E':f=1
#     else:
#         if f:c+=1;f=0
print(open(0).read().count('EW'))