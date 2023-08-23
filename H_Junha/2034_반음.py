import sys

N = int(sys.stdin.readline())

score = []
note = "A0BC0D0EF0G0"

for test_case in range(N):
    score.append(int(sys.stdin.readline()))

for i in range(len(note)):
    now = i
    start = note[now]
    for s in score:
        now = (now + s) % 12 # now == 현재 위치 index
        if note[now] == "0":
            start = "X"
            end = "X"
        else:
            end = note[now]

    if start != "X" and end != "X":
        print(start, end)    
                
