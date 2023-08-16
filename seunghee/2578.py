import sys
data = []
nums = []
bingo = [[0]*5 for _ in range(5)] 

for _ in range(5):
    data.extend(sys.stdin.readline().strip().split(' '))
for _ in range(5):
    nums.extend(sys.stdin.readline().strip().split(' '))

def line(bingo):
    cnt = 0
    if (bingo[4][0]+bingo[3][1]+bingo[2][2]+bingo[1][3]+bingo[0][4]) ==5 :#하좌-> 상우
        cnt += 1

    if (bingo[0][0]+bingo[1][1]+bingo[2][2]+bingo[3][3]+bingo[4][4]) ==5:#상좌->하우
        cnt += 1
    # 행별 확인
    for i in range(5):
        if sum(bingo[i]) == 5:
            cnt += 1 

    revered_bingo = list(zip( *bingo ))
    # 열별 확인
    for j in range(5):
        if sum(revered_bingo[j]) == 5:
            cnt += 1 

    if cnt >= 3:
        return True
    else:
        return False

for i, num in enumerate(nums):
    if i >= 4: # 빙고 찾기
        if line(bingo):# 3개 이상 나옴
            print(i)
            break
    idx = data.index(num)
    bingo[idx//5][idx%5] = 1
# 0~4   [0][i]
# 5~9   [i//5][i%5] i//5
# 10~14  [i//5]
# 15~19   [i//5]
# 20~24   [i//5]
