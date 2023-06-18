# 0614 45분까지
n, tesu, p = map(int, input().split())
if n != 0:
    scorelist = list(map(int, input().split()))
else:
    scorelist = list()


newlist = scorelist[:]
newlist.append(tesu)
scorelist.sort(reverse=True)
newlist.sort(reverse=True)

rank = scorelist[:p]
ranktesu = newlist[:p]

ranking = 0

cnt = 0
for i in rank:
    if len(str(i)) >= 2:
        cnt += len(str(i)) - 1


if tesu in rank:
    if tesu == rank[-1]:
        if p >= n + 1:
            print(ranktesu.index(tesu) + 1)
        else:
            print("-1")
    else:
        print(ranktesu.index(tesu) + 1)
else:
    if tesu in ranktesu:
        print(ranktesu.index(tesu) + 1)
    else:
        print("-1")
