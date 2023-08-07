import sys
N = int(sys.stdin.readline().strip())
string = sys.stdin.readline().strip()

alpa = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alpa = list(alpa)

data = {}
for a in alpa[:N]:
    num = sys.stdin.readline().strip()
    data[a] = int(num)

ans = 0
for char in string:
    number = ''
    if char in alpa:
        number += alpa[char]

    elif char == '+':

eval('수식')