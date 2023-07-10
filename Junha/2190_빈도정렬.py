import sys
from collections import defaultdict

N,C = list(map(int,sys.stdin.readline().split()))
MSG = list(map(int,sys.stdin.readline().split()))

msg_dict = defaultdict(int)

for m in MSG:
    msg_dict[m] += 1

msg_dict = sorted(msg_dict.items(), key = lambda item: item[1],reverse = True)
for key, value in msg_dict:
    print((str(key)+" ")*value,end="")
    