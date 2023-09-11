# # standard solution
# *A,=open(0).read().split()
# A=A[:-1]
# for a in A:
#     n=len(a)
#     b,d=a[:n//2][::-1],a[(n+1)//2:]
#     if int(b)>int(d):print(int(b)-int(d))
#     elif int(b)<int(d):
#         k=1
#         while 1:
#             e=str(int(a)+k).zfill(n)
#             b,d=e[:n//2][::-1],e[(n+1)//2:]
#             if int(b)==int(d):print(k);break
#             k+=1
#     else:print(0)

# the best solution
*A,=open(0).read().split();A=A[:-1]
def B(a):
    e=[];n=len(a)
    for i in range(n//2):
        b,d=a[i],a[-1-i]
        if b<d:e+=[(10+int(b)-int(d))*10**i]
        else:e+=[(int(b)-int(d))*10**i]
        a=str(int(a)+e[i]).zfill(n)
    if n%2==0 and a[i]>a[i+1]:e+=[10**i];a=str(int(a)+e[-1]).zfill(n)
    return sum(e)if a[:n//2][::-1]==a[(n+1)//2:]else sum(e)+B(a)
for a in A:print(B(a))