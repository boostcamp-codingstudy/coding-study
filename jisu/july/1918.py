import sys

input = sys.stdin.readline
from collections import deque

inp = list(input().rstrip())
susicstack = list()
complete = ""

susic = ["+", "-", "*", "/", "(", ")"]
for i in inp:
    if i.isalpha():
        complete += i
    else:
        if i == "(":
            susicstack.append(i)
        elif i in ["*", "/"]:
            while (len(susicstack) != 0) and (susicstack[-1] in ["*", "/"]):
                complete += susicstack.pop()
            susicstack.append(i)
        elif i in ["+", "-"]:
            while (len(susicstack) != 0) and (susicstack[-1] != "("):
                complete += susicstack.pop()
            susicstack.append(i)
        else:
            while (len(susicstack) != 0) and (susicstack[-1] != "("):
                complete += susicstack.pop()
            susicstack.pop()
while susicstack:
    complete += susicstack.pop()
print(complete)
