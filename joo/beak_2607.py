import sys
input = sys.stdin.readline

# 입력 받는 단어의 개수
n = int(input())
# 맨 첫번째 단어. 꼭 strip()을 해야 마지막에 '\n'이 안들어감
# list()로 감싸주면 문자열이 하나씩 리스트로 들어간다.
# ['d', 'o', 'g']
first = list(input().strip())

answer = 0
for _ in range(n-1): # 한 개 적게 단어를 받음
    # 이거 복제 조심해야 함. 그냥 변수 넣으면 안됨.
    copy_first = first[:]
    word = list(input().strip()) # 리스트 안에 글자 하나씩 넣음
    c = 0 # 남는 글자 개수
    for i in word: # word에서 한 글자씩 빼냄
        if i in copy_first: # 만약에 first에 있으면 
            copy_first.remove(i) # first에서 i를 지움
        else: # first에 글자 없는 경우
            c += 1
    """ 
    문제를 잘못봄. 한 단어를 변경할 수도 있는 거였음
    # for문이 다 돌고 난 후 first에 글자가 없고 남는 글자가 1개 이하
    if len(copy_first) == 0 and c <= 1:
        answer += 1
    # 남는 글자 없고 first에 남은게 하나 이하
    elif len(copy_first) <= 1 and c == 0:
        answer += 1
    """
    if c < 2 and len(copy_first) < 2:
        answer += 1

print(answer)