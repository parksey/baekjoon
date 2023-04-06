def change(day):
    return ''.join(list(map(lambda x: "0"+str(x) if x <10 else str(x), day)))

def compare(today, finalDay):
    today = change(today)
    finalDay = change(finalDay)
    return today > finalDay

def isDelete(today, day, caseMonth):
    dayList = list(map(int, day.split(".")))
    
    year = caseMonth//12
    caseMonth %= 12
    
    dayList[2] -= 1
    if dayList[2] < 1:
        dayList[2] = 28
        dayList[1] -= 1
    
    dayList[1] += caseMonth
    dayList[0] += dayList[1]//12
    dayList[1] %= 12
    if dayList[1] < 1:
        dayList[1] = 12
        dayList[0] -= 1
    
    dayList[0] += year
    return compare(today, dayList)
    

    
def solution(today, terms, privacies):
    answer = []
    today = list(map(int, today.split(".")))

    termsMap = {}
    
    for term in terms:
        case, month = term.split()
        termsMap[case] = int(month)
    
    for index, privacie in enumerate(privacies):
        day, case = privacie.split()
        
        if isDelete(today, day, termsMap[case]):
            answer.append(index+1)
        
    return answer