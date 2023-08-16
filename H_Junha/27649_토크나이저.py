import sys
from collections import deque

# S = deque(sys.stdin.readline())

sep = ["<",">","&&","||","(",")"," "]
# token = []
# new_str = ""
# new_s = ""
# while S:
#     temp = S.popleft()
    
#     if temp == "&" or temp =="|":
#         new_s = temp
#         new_s += S.popleft()
#     else:
#         new_s = temp
    
    
#     if new_s == " ":        
#         token.append(new_str)
#         new_str = ""
#     elif new_s in sep:
#         token.append(new_str)
#         token.append(new_s)
#         new_str = ""
#     else:
#         new_str += new_s
        
# token.append(new_str)

# token = list(filter(None, token))

# print(" ".join(token))

S = sys.stdin.readline()
for i in sep:
    S = S.replace(i, f" {i} ")

print(" ".join(S.split()))