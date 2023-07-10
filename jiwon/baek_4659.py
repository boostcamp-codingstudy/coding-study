# https://www.acmicpc.net/problem/4659
# 비밀번호 발음하기
# 정규식 아이디어 활용

import sys
import re

while True:
    text = sys.stdin.readline().strip()
    if text == "end":     # 종료조건
        break

    case1 = re.findall(r"a|e|i|o|u", text)
    case2 = re.findall(r"([a|e|i|o|u]{3})|([^a|e|i|o|u]{3})", text)
    case3 = re.findall(r"([a-df-np-z])\1", text)

    if len(case1) != 0 and len(case2) == 0 and len(case3) == 0:
        print(f"<{text}> is acceptable.")
    else:
        print(f"<{text}> is not acceptable.")
