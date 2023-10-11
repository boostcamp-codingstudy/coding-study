def solution(F):
    S=[]
    for i,f in enumerate(F):
        h,n,t,p='','','',0
        for c in f:
            if c.isdigit():
                if p<2:n+=c;p=1
                else:t+=c
            else:                
                if p:t+=c;p=2
                else:h+=c
        S+=[[i,h,n,t]]
    S.sort(key=lambda e:[e[1].lower(),int(e[2])])
    return [F[s[0]] for s in S]

# checking answers
TCs =   [
            (
                ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"], 
                ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]
            ),
            (
                ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"],
                ["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"]
            )
        ]
for i, (input_, output) in enumerate(TCs):
    assert solution(input_) == output, f'The result differs from TC#{i}\ninput:{input_}\noutput:{output}'