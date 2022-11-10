T = int(input())

def solve(n):
    result = [[0]*(i+1) for i in range(n)]
    
    result[0][0] = 1
    print(*result[0])
    for i in range(1,n):
        for j in range(len(result[i])):
            if j == 0 or j == len(result[i])-1:
                result[i][j] = 1
            else:
                result[i][j] = result[i-1][j-1] + result[i-1][j]
                
        print(*result[i])

for i in range(T):
    N = int(input())
    print("#{}".format(i+1))
    solve(N)