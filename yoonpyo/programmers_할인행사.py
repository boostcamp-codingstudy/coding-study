def dict_count(dict1,dict2,want):
    if dict1.keys()==dict2.keys():
        for i in want:
            if dict1[i]>dict2[i]:
                return False
        return True

def solution(want, number, discount):
    answer = 0
    s=0
    dict1={}
    for i in range(len(number)):
        dict1[want[i]]=number[i]
    while s<=len(discount)-10:
        dict2={}
        for i in range(s,s+10):
            if discount[i] not in dict2:
                dict2[discount[i]]=1
            else:
                dict2[discount[i]]+=1
        s+=1
        if dict_count(dict1,dict2,want)==True:
            answer+=1
            
    return answer