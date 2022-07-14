N = int(input())

result = []

for i in range(N):
    data = input()
    list_cnt = int(input())
    isR = False
    isE = False
    
    temp = input()[1:-1]
    if not temp:
        if 'D' in data:
            result.append("error")
        elif 'D' not in data:
            result.append("[]")
    else:
        case = temp.split(",")
        case_len =len(case)
        for d in data:
            if d == 'R':
                isR = not isR
            
            if d == 'D':
                if case_len == 0:
                    isE = True
                    break
                elif isR:
                    case_len -= 1
                    del case[-1]
                else:
                    case_len -= 1
                    del case[0]
        if isE:
            result.append("error")
        elif isR:
            result.append("["+','.join(case[::-1])+"]")
        else:
            result.append("["+','.join(case)+"]")
        
print('\n'.join(result))