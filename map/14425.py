import sys
N, M = map(int, input().split())

string = {}
for i in range(N):
    temp = sys.stdin.readline().strip()
    string[temp] = temp

cnt = 0
for _ in range(M):
    temp = sys.stdin.readline().strip()
    if temp in string:
        cnt += 1
print(cnt)