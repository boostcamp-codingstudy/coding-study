# 11:15
# 숫자(n)가 나오면 앞에꺼 n개 , 앞에꺼가 문자면 그냥 그자리에 n-1개의 문자, ()여도 그자리에 n-1개의 문자
chemy = input()
pre = ""
secret = list()
lastsecret = list()
stack = [0]
norm = "*"
sum = 0
total = 0
adi = {"H": 1, "C": 12, "O": 16}
for i in chemy:
    if i == "(":
        stack.append(0)
    elif i == ")":
        tmp_sum = 0
        t = stack.pop()
        while t > 0:
            t += stack.pop()
        stack[-1] += tmp_sum
    elif i in ["2", "3", "4", "5", "6", "7", "8", "9"]:
        stack[-1] *= int(i)
print(total)
# if i in ['2','3','4','5','6','7','8','9']:
#     if pre == ')':
#         for j in range(int(i)):
#             secret.append(norm)
#     i = '*'
# if i=='(':
