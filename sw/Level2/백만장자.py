T = int(input())

def solve(day):
    cost = list(map(int, input().split()))
    
    calcCost = [0] * day
    i = day-1
    while i > -1:
        # 1 4 2 3 5 2 3
        j = i-1

        while j > -1:
            calcCost[j] = calcCost[j+1]
            if cost[i] > cost[j]:
                calcCost[j] += (cost[i] - cost[j])
            else:
                break
            j-=1
        i = j         
                
    return calcCost[0]
        # 0 0 0 0 1 1 0  

for i in range(T):
    day = int(input())
    
    print("#{} {}".format(i+1, solve(day)))