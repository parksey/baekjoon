N = int(input())

have = list(map(int, input().split()))
have.sort()
M = int(input())

check_list = list(map(int,input().split()))

def check(c,start, end):
    if start >= end:
        return 0
    n = (start+end)//2
    if have[n] == c:
        return 1

    re = 0

    if have[n] > c:
        re =check(c,0,n)
    else:
        re =check(c,n+1,end)
    return re


for c in check_list:
    print(check(c,0,N), end=' ')    
