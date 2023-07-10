n = int(input())
originn = n
st = 0
ed = 1
while not ((2**st) < n <= (2**ed)):
    st += 1
    ed += 1
cnt = 0
while not (n == 0):
    n = n % (2**st)
    st -= 1
    cnt += 1
if originn == 2**ed:
    cnt = 0
print(2**ed, cnt)
