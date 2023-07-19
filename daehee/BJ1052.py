N,K=map(int,input().split())
B=bin(N)[2:];i,k=0,0
for b in B:
    i+=1
    if int(b):k+=1
    if k==K:break
C=B[i:]
print(2**len(C)-int(C,2)if C.count('1')else 0)