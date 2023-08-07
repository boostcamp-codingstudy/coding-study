import sys

notation = sys.stdin.readline()
form = "*/+-"

# 괄호 만들기
for i in form:
    for idx,n in enumerate(notation):
        if n == i:
            nxt = idx+1
            if not(notation[idx-1] in "()") and not(notation[nxt] in "()"):
                ori_str = notation[idx-1] + n + notation[nxt]
                new_str = "("+ notation[idx-1] + n + notation[nxt] + ")"
            elif notation[idx-1] in "()" and notation[nxt] in "()":
                right = idx + 1
                left = idx - 1
                while notation[right] != ")":
                    right += 1
                while notation[left] != "(":
                    left -= 1
                ori_str = notation[left:right]
                new_str = "(" + notation[left:right] + ")"
            else:
                while notation[nxt] != ")":
                    nxt += 1
                ori_str = notation[idx-1] + n + notation[idx+1:nxt]
                new_str = "("+ notation[idx-1] + n + notation[idx+1:nxt] + ")"
            print(new_str)
            notation = notation.replace(ori_str, new_str)
    
