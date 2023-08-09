N = int(input())
NUM = int(input())
map = [[0 for i in range(N)] for j in range(N)]
map[int(N/2)][int(N/2)] = 1

odds = [i for i in range(1,N+2,2)]
odds.reverse()
x = [1,0,-1,0]
y = [0,1,0,-1]

for idx,odd in enumerate(odds[:-1]):
    nx, ny = idx,idx
    move = 0
    count = 0
    start = odd*odd
    end = (odd-2)*(odd-2)
    for i in range(start,end,-1):
        map[nx][ny] = i
        
        nx += x[move]
        ny += y[move]
        count += 1

        if count == odd-1:
            move += 1
            count = 0
            
        
for x,i in enumerate(map):
    for y,j in enumerate(i):
        if j == NUM:
            answer = [x+1,y+1]
        print(j,end=" ")
    print()   

for a in answer:
    print(a,end=" ")