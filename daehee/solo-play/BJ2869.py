# my answer
# a=*map(int,input().split()),
# b=(a[2]-a[0])//(a[0]-a[1])
# c=a[2]-b*(a[0]-a[1])
# i=0
# while c>0:
#     i+=1
#     c-=a[0]
#     if c<=0:break
#     c+=a[1]
# print(b+i)

# best answer
a,b,h=map(int,input().split())
print((h-b-1)//(a-b)+1)