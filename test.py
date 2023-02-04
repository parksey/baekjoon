'''
ㅡ
|

1 1
2 || =      2
3 ||| =| |=   3
4 |||| =|| ||= == |=| 5 
'''

N = int(input())
countList = [0] * (N+1)

def solve():
    countList[1] = 1
    if N == 1:
        return 1
    countList[2] = 2
    if N == 2:
        return 2
    
    for i in range(3, N+1):
        countList[i] = (countList[i-1] + countList[i-2]) % 10_007
solve()
print(countList[N])