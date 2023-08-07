# # standard solution
# n=int(input());D={n:0}
# for i in range(n-1,0,-1):
#     D[i]=min(D.get(i+1,n),D.get(i*2,n),D.get(i*3,n))+1
# print(D.get(1))

# # standard solution 2
# n=int(input());D=[0,0]+[n]*(n-1)
# for i in range(1,n+1):
#     if i+1<=n:D[i+1]=min(D[i]+1,D[i+1])
#     if i*2<=n:D[i*2]=min(D[i]+1,D[i*2])
#     if i*3<=n:D[i*3]=min(D[i]+1,D[i*3])
# print(D[n])

# # faster solution
# n=int(input());D=[n]*3*n;D[n]=0
# for i in range(n-1,0,-1):
#     D[i]=min(min(D[i+1],D[i*2],D[i*3])+1,D[i])
# print(D[1])

# the best solution
n=int(input());d={0:0,1:0}
def D(n):
    if n in d:return d[n]
    d[n]=1+min(D(n//3)+n%3,D(n//2)+n%2)
    return d[n]
print(D(n))

# # the best solution analysis
# max_depth,max_depth2=0,0
# n=int(input());d={0:0,1:0};d2={1:0,2:1}
# def D(n,depth):
#     global max_depth
#     if depth>max_depth:max_depth=depth
#     if n in d:return d[n]
#     d[n]=1+min(D(n//3,depth+1)+n%3,D(n//2,depth+1)+n%2)
#     return d[n]
# def D2(n,depth):
#     global max_depth2
#     if depth>max_depth2:max_depth2=depth
#     if n in d2:return d2[n]
#     d2[n]=1+min(D2(n//3,depth+1)+n%3,D2(n//2,depth+1)+n%2)
#     return d2[n]
# print(D(n,0),max_depth)
# print(D2(n,0),max_depth2)