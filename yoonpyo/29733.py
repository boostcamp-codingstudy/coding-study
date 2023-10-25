r,c,h=map(int,input().split())
cube=[[[0]*c for _ in range(r)] for _ in range(h)]
for i in range(h):
    for j in range(r):
        cube[i][j]=list(map(str,input()))
answer=cube
for i in range(h):
    for j in range(r):
        for k in range(c):
            cnt=0
            if cube[i][j][k]=='.':
                if i!=0: #7개
                    if cube[i-1][j][k]=='*':
                        cnt+=1
                    if j!=r-1 and cube[i-1][j+1][k]=='*': 
                        cnt+=1
                    if j!=0 and cube[i-1][j-1][k]=='*':
                        cnt+=1
                    if k!=c-1 and cube[i-1][j][k+1]=='*':
                        cnt+=1
                    if k!=0 and cube[i-1][j][k-1]=='*':
                        cnt+=1
                    if j!=r-1 and k!=c-1 and cube[i-1][j+1][k+1]=='*': 
                        cnt+=1
                    if j!=r-1 and k!=0 and cube[i-1][j+1][k-1]=='*': 
                        cnt+=1
                if j!=0: #8개
                    if cube[i][j-1][k]=='*':
                        cnt+=1
                    if k!=c-1 and cube[i][j-1][k+1]=='*':
                        cnt+=1
                    if k!=0 and cube[i][j-1][k-1]=='*':
                        cnt+=1
                    if i!=h-1 and cube[i+1][j-1][k]=='*':
                        cnt+=1  
                    if i!=0 and k!=c-1 and cube[i-1][j-1][k+1]=='*': 
                        cnt+=1
                    if i!=0 and k!=0 and cube[i-1][j-1][k-1]=='*': 
                        cnt+=1
                    if i!=h-1 and k!=c-1 and cube[i+1][j-1][k+1]=='*': 
                        cnt+=1
                    if i!=h-1 and k!=0 and cube[i+1][j-1][k-1]=='*': 
                        cnt+=1                        
                if k!=0: #4개
                    if cube[i][j][k-1]=='*':
                        cnt+=1
                    if i!=h-1 and cube[i+1][j][k-1]=='*':
                        cnt+=1
                    if j!=r-1 and cube[i][j+1][k-1]=='*':
                        cnt+=1
                    if i!=h-1 and j!=r-1 and cube[i+1][j+1][k-1]=='*':
                        cnt+=1
                if i!=h-1:
                    if cube[i+1][j][k]=='*':
                        cnt+=1
                    if j!=r-1 and cube[i+1][j+1][k]=='*':
                        cnt+=1
                    if k!=c-1 and cube[i+1][j][k+1]=='*':
                        cnt+=1
                    if j!=r-1 and k!=c-1 and cube[i+1][j+1][k+1]=='*': 
                        cnt+=1
                if j!=r-1 and cube[i][j+1][k]=='*': 
                    cnt+=1
                if k!=c-1 and cube[i][j][k+1]=='*':
                    cnt+=1
                if j!=r-1 and k!=c-1 and cube[i][j+1][k+1]=='*': 
                    cnt+=1
                answer[i][j][k]=cnt%10
for i in range(h):
    for j in range(r):
        print(*answer[i][j],sep='')