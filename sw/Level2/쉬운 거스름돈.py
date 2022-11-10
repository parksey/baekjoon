T = int(input())

def solve():
    PAY = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    moneyList = [0]*8
    
    money = int(input())
    
    for i in range(8):
        moneyList[i] = money // PAY[i]    
        money %= PAY[i] 
    
    return moneyList

for i in range(T):
    print("#{}".format(i+1))
    print(*solve())