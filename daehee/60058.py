def solution(p):
    if len(p):
        u,v=cut(p)
        return '('+solution(v)+')'+flip(u) if check(u) else u+solution(v)
    else:return ''
      
def cut(w):
    balance=0
    for i in range(len(w)):
        balance+=1 if w[i]=='(' else -1
        if balance==0:return w[:i+1],w[i+1:]
        
def check(w):
    balance=0
    for i in range(len(w)):
        balance+=1 if w[i]=='(' else -1
        if balance<0:return balance
    return balance

def flip(w):
    return ''.join([')'if w[i]=='('else'('for i in range(1,len(w)-1)])

# checking answers
TCs =   [
            (
                "(()())()", 
                "(()())()"
            ),
            (
                ")(", 
                "()"
            ),
            (
                "()))((()", 
                "()(())()"
            )
        ]
for i, (input_, output) in enumerate(TCs):
    assert solution(input_) == output, f'The result differs from TC#{i}\ninput:{input_}\noutput:{output}'