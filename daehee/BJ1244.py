'''
여학생이 입력 되었을 때, 여학생의 위치로부터 왼쪽 switch와 오른쪽 switch의 상태를 각각 ls, rs라고 한다.
여학생의 위치로부터 switch 배열의 가까운 쪽까지 좌우 대칭 영역을 탐색 한다.
ls와 rs의 값에 따라 아래와 같이 XOR 연산 된다.
if ls == rs, then ls ^ rs == 0
if ls != rs, then ls ^ rs == 1 
ls ^ (ls ^ rs) == ls ^ ls ^ rs == rs
rs ^ (ls ^ rs) == rs ^ ls ^ rs == ls
따라서 탐색 가능 최대 좌우 대칭 영역까지 모두 아래와 같이 적용 가능하다.
ls = 1 ^ rs
rs = 1 ^ ls
좌우 switch 값이 서로 다른 경우가 발생 하는 위치까지 탐색 및 flip 한다.

※ 좌우 대칭 탐색 영역 이내에 좌우 switch 값이 서로 다른 경우, 
이후 탐색 영역에서 다시 switch 값이 서로 같은 경우가 나타나더라도, 
switch 상태를 flip 하면 안되므로 조건문 없이 XOR 연산만으로 적용 불가
'''
def solution():
    n_switches = int(input())
    switches = [int(e) for e in input().split()]
    n_students = int(input())
    students = []
    for i in range(n_students):
        students.append([int(e) for e in input().split()])
    
    for student in students:
        if student[0] == 1:
            for i in range(n_switches // student[1]):
                switches[(i + 1) * student[1] - 1] ^= 1
        else:
            for i in range(min(student[1], n_switches + 1 - student[1])):
                l, r = student[1] - i - 1, student[1] + i - 1
                ls, rs = switches[l], switches[r]
                if ls != rs: break
                switches[l] = 1 ^ rs
                switches[r] = 1 ^ ls

    for i, switch in enumerate(switches):
        print(switch, end=' ')
        if (i + 1) % 20 == 0:
            print()
solution()