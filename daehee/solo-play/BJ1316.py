# standard solution
A=open(0).read().split()
n=A[0];c=0
for a in A[1:]:
    f=1;D=[0]*26
    for i in range(len(a)):
        o=ord(a[i])-ord('a')
        if D[o]:
            if i>1 and p!=o:f=0;break
        else:D[o]+=1
        p=o
    if f:c+=1
print(c)

# # the best solution
# print(sum([*x]==sorted(x,key=x.find)for x in open(0))-1)