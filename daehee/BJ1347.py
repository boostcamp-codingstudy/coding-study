n,s=int(input()),input()
h=w=i=j=0
d,k=[[1,0],[0,-1],[-1,0],[0,1]],0
I,J=[0],[0]
for c in s:
    if c=='L':k=(k+3)%4
    elif c=='R':k=(k+1)%4
    else:i+=d[k][0];j+=d[k][1]
    I+=[i];J+=[j]
R,C=min(I),min(J)
h,w=max(I)-R+1,max(J)-C+1
m=[['#']*w for _ in range(h)]
for i,j in zip(I,J):
    m[i-R][j-C]='.'
# print(''.join([''.join(e)+'\n'for e in m]))
for e in m:
    for c in e:print(c,end='')
    print()