from datetime import datetime
import math
def solution(fees, records):
    answer = []
    records.append("24:24 99999 III")
    for i in range(len(records)):
        records[i]=records[i].split(" ")
    records.sort(key=lambda x:x[1])
    car_number=records[0][1]
    fee=0
    money=[]
    for i in range(len(records)):
        if i==len(records)-1:
            money.append(fee)
        if records[i][2]=="OUT":
            time1 = datetime.strptime(records[i-1][0], "%H:%M")
            time2 = datetime.strptime(records[i][0], "%H:%M")
            fee+=(time2-time1).total_seconds()/60
        elif records[i][2]=="IN":
            if records[i-1][1]!=records[i][1]:
                money.append(fee)
                fee=0
                car_number=records[i][1]
            if records[i+1][1]!=car_number:
                time3 = datetime.strptime(records[i][0], "%H:%M")
                time4 = datetime.strptime("23:59", "%H:%M")
                fee+=(time4-time3).total_seconds()/60
                
    for fee in money[1:]:
        if fee<=fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1]+math.ceil((fee-fees[0])/fees[2])*fees[3])
    return answer