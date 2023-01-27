T = int(input())

MONTH = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def solve():
    day = list(map(int, input().split()))
    if day[0] == day[2]:
        return day[3] - day[1] + 1
    
    ret = sum(MONTH[day[0]+1: day[2]])

    return ret + (MONTH[day[0]] - day[1] + 1) + (day[3])

for i in range(T):
    print("#{} {}".format(i+1, solve()))