'''
n by n 행렬을 만들고 중심에 1을 저장 한다.
상, 우, 하, 좌 순서로 순차적으로 방향을 바꾼다.
행렬에 이미 값이 써진 경우 기존 방향을 유지 한다.
찾는 값이 현재 값과 같을 경우, 위치를 저장 한다.
완료 된 행렬과 찾는 값의 위치를 출력 한다.
'''
def solution():
    n = int(input())
    order = int(input())
    matrix = [[0] * n for i in range(n)]
    dirs, dir_id = [[-1, 0], [0, 1], [1, 0], [0, -1]], -1
    target_pos, pos = [], [n // 2] * 2
    
    for i in range(n * n):
        matrix[pos[0]][pos[1]] = i + 1
        if order == i + 1: target_pos = pos[:]
        dir_id_next = (dir_id + 1) % len(dirs)
        if matrix[pos[0] + dirs[dir_id_next][0]][pos[1] + dirs[dir_id_next][1]] == 0:
            dir_id = dir_id_next
        pos = [sum(e) for e in zip(pos, dirs[dir_id])]
        
    for i in range(n):
        for j in range(n):
            print(matrix[i][j], end = ' ')
        print()
    print(target_pos[0] + 1, target_pos[1] + 1)

solution()