from collections import deque # deque 사용해야 rotate 함수 사용 가능
def rotate_right(num, d):
    if num > 4 or gears[num - 1][2] == gears[num][6]:
        return

    if gears[num - 1][2] != gears[num][6]:
        rotate_right(num + 1, -d)
        gears[num].rotate(d)
        
def rotate_left(num, d):
    if num < 1 or gears[num][2] == gears[num + 1][6]:
        return

    if gears[num][2] != gears[num + 1][6]:
        rotate_left(num - 1, -d)
        gears[num].rotate(d)


gears = {}
for i in range(1, 5):
    gears[i] = deque((map(int, input())))
k=int(input())
for i in range(k):
    num, d = map(int, input().split())
    rotate_right(num + 1, -d)
    rotate_left(num - 1, -d)
    gears[num].rotate(d)

score=0
for i in range(4):
    if gears[i+1][0]==1:
        score+=(2**i)
print(score)