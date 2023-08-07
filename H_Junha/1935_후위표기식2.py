import sys
from collections import deque



N = int(sys.stdin.readline())
C = list(sys.stdin.readline().rstrip())
ARR = []
alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

alpha_dict = {}

for i in range(N):
    value = sys.stdin.readline().rstrip()
    alpha_dict[alphabet[i]] = value
    
new_C = []
for i in range(len(C)):
    if C[i] in alphabet:
        C[i] = alpha_dict[C[i]]

# print(C)
C = deque(C)
stack = deque()

while C:
    temp = C.popleft()
    
    stack.append(temp)
    if not(temp.isdigit()):
        a = stack.pop()
        b = stack.pop()
        c = stack.pop()
        stack.append(str(eval(c+a+b)))
            
        
print(f"{float(stack[0]):0.2f}")
    