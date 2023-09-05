def solution(places):
    answer = []
    for i in places:
        waitroom=[]
        for t in i:
            waitroom.append(list(t))
        key=1
        for j in range(5):
            if key==0:
                break
            for k in range(5):
                if key==0:
                    break
                if waitroom[j][k]=='P':
                    if j<4:
                        if waitroom[j+1][k]=='P':
                            key=0
                            break
                        if j<3 and waitroom[j+2][k]=='P' and waitroom[j+1][k]=='O':
                            key=0
                            break
                    if k<4:
                        if waitroom[j][k+1]=='P':
                            key=0
                            break
                        if k<3 and waitroom[j][k+2]=='P' and waitroom[j][k+1]=='O':
                            key=0
                            break
                    if j<3 and k<3:
                        if waitroom[j+1][k+1]=='P' and (waitroom[j][k+1]=='O' or waitroom[j+1][k]=='O'):
                            key=0
                            break
                    if j<3 and k>=1:
                        if waitroom[j+1][k-1]=='P' and (waitroom[j][k-1]=='O' or waitroom[j+1][k]=='O'):
                            key=0
                            break
        if key==0:
            answer.append(0)
        elif key==1:
            answer.append(1)
    return answer