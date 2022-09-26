from collections import deque
import sys

V,E = map(int, input().split())
start = int(input())

INF = 9999999
v_list = [INF]*(V+1)
visit = [0]*(V+1)


line = [[] for i in range(V+1)]
for i in range(E):
    s,e,a = map(int, input().split())
    line[s].append([e,a])

def find():
    min = INF
    index = 0
    for i in range(1,V+1):
        if visit[i]: continue
        
        if v_list[i] < min:
            min = v_list[i]
            index = i
    return index
        
def solve(start):
    v_list[start] = 0
    for i in range(V):
        index = find()
        visit[index] = 1
        for v in line[index]:
            if v_list[index]+v[1] <  v_list[v[0]]:
                v_list[v[0]] = v_list[index] + v[1]

solve(start)
for v in v_list[1:]:
    print("INF") if v == INF else print(v)
