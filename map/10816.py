import sys
input = sys.stdin.readline

N = int(input())

have = list(map(int, input().split()))
have.sort()
M = int(input())

check_list = list(map(int,input().split()))

dic = {}
for n in have:
    if n in dic:
        dic[n] += 1
    else:
        dic[n] = 1

def check(c,start, end):
    if start >= end:
        return False
    n = (start+end)//2
    
    if have[n] == c:
        return True
    
    if have[n] > c:
        return check(c,start,n)
    else:
        return check(c,n+1,end)
    
for c in check_list:
    if check(c,0,N):
        print(dic[c], end=' ')
    else:
        print("0 ",end="")