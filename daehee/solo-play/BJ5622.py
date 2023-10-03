# # standard solution using hard coding
# D={' ':1,
#    'A':2,'B':2,'C':2,
#    'D':3,'E':3,'F':3,
#    'G':4,'H':4,'I':4,
#    'J':5,'K':5,'L':5,
#    'M':6,'N':6,'O':6,
#    'P':7,'Q':7,'R':7,'S':7,
#    'T':8,'U':8,'V':8,
#    'W':9,'X':9,'Y':9,'Z':9}
# s=0
# for c in input():s+=D[c]+1
# print(s)

# standard solution using hard coding 2
A=[2]*3+[3]*3+[4]*3+[5]*3+[6]*3+[7]*4+[8]*3+[9]*4
print(sum([A[ord(c)-65]+1 for c in input()]))

# # the best solution
# print(sum((c-(c>82)-(c>89)-56)//3 for c in map(ord,input())))