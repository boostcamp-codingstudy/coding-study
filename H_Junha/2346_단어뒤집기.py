import sys
from collections import deque

S = deque(sys.stdin.readline())

special = "<>"
blank = " "

answer = ""
temp_letter = ""
letter = S.popleft()

while S:
    if letter == "<":
        while letter != ">":            
            answer += letter
            letter = S.popleft()
        answer += letter
    else:
        while True:
            if letter == "<":
                break
            temp_letter += letter
            letter = S.popleft()
            if not(S):
                break
        answer += "".join(reversed(temp_letter))
    
        
    


    # answer += "".join(reversed(temp_letter))
        
print(answer)