word = "((CH)2(OH2H)(C(H))O)3"

chemical_dict = {"H":1,
                 "C":12,
                 "O":16}

stack = []

for w in word:

    if w == "(":
        stack.append(w)
    elif w == ")":
        check = 0
        while True:
            t = stack.pop()
            if t == "(":
                break
            check += t
        stack.append(check)
        
    elif w in chemical_dict.keys():
        stack.append(chemical_dict[w])
    else:
        stack[-1] *= int(w)
    print(stack)
print(sum(stack))