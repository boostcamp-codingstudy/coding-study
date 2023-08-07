import sys

n = int(sys.stdin.readline())
strlist = list(map(str, sys.stdin.readline().rstrip()))
strlist.sort()
cnt = 0

for i in range(n - 1):
    tmplist = list(map(str, sys.stdin.readline().rstrip()))
    tmplist.sort()

    ttmplist = tmplist[:]  # 깊은 복사

    # 구성하는 알파벳과 각 알파벳의 개수가 같을 경우 먼저 count
    if strlist == tmplist:
        cnt += 1
        continue

    copyl = strlist[:]
    copyr = strlist[:]

    # 주어진 리스트와 해당 i번째의 리스트간의 차이를 구함 (copyl - tmplist)
    for i in range(len(copyl)):
        if copyl[i] in tmplist:
            tmplist.remove(copyl[i])
            copyl[i] = "0"  # copyl의 index를 기준으로 for 문이 돌아가므로 remove해줄 경우 제대로 검사를 못하는 경우가 생겨 0으로 변경
    copycnt = 0
    for i in copyl:
        if i != "0":
            copycnt += 1

    # 주어진 리스트와 해당 i번째의 리스트간의 차이를 구함 (tmplist - copyl)
    for i in range(len(ttmplist)):
        if ttmplist[i] in copyr:
            copyr.remove(ttmplist[i])
            ttmplist[i] = "0"  # 마찬가지로 0으로 변경 (for 문이 끝난 다음 count )
    ttmpcnt = 0
    for i in ttmplist:
        if i != "0":
            ttmpcnt += 1

    # copycnt와 ttmpcnt가 둘 중 하나라도 2를 넘어가지 않는 경우를 찾아서 count
    if copycnt * ttmpcnt == 1:
        cnt += 1
    elif copycnt * ttmpcnt == 0:
        if copycnt == 1:
            cnt += 1
        elif ttmpcnt == 1:
            cnt += 1

print(cnt)
