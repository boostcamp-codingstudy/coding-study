import sys
from collections import Counter
name = list(str(sys.stdin.readline().strip()))
ans = []
name_counter = Counter(name)

if len(name) % 2 == 0: # 짝수개임 - 모든 단어개수가 짝수개여야됌
    for char, cnt in sorted(name_counter.items()): # 사전순으로 정렬
        if cnt % 2 != 0: # 홀수개가 있다
            print("I'm Sorry Hansoo")
            exit(0)
        else: # 짝수개이다
            for i in range(int(cnt/2)): # 반절만 넣음
                ans.append(char)
    print(''.join(ans[:]+ ans[::-1]))
else:
    odd_char = [] # 중심에 있어야되는 단어임 - 홀수개가 들어가야됌
    # AABBBCC -> ABCBCBA
    # 어차피 홀수개인 단어가 1번만 있어야 가능한거아닌가?....
    for char, cnt in sorted(name_counter.items()):
        if cnt % 2 != 0: # 홀수개가 있다
            odd_char.append(char)
            cnt -= 1

        if len(odd_char) > 1: # 홀수인게 1개 초과일때
            print("I'm Sorry Hansoo")
            exit(0)

        for i in range(int(cnt/2)): # 반절만 넣음
            ans.append(char)
    print(''.join(ans[:]+ odd_char + ans[::-1]))