from collections import deque


N, E = map(int, input().split())

mapping = [[] for i in range(N+1)]
for i in range(E):
    a,b,c = map(int, input().split())
    
    mapping[a].append([b,c])
    mapping[b].append([a,c])
    
first, second = map(int, input().split())
INF = 9999999999999
def find(visit,node):
    min = INF
    index = 0
    for i in range(1, N+1):
        if visit[i]: continue
        if min >= node[i]:
            min = node[i] 
            index = i 
    return index

def solve(start):    
    node = [INF]* (N+1)
    visit = [0] * (N+1)

    for i in mapping[start]:
        if node[i[0]] > i[1]:
            node[i[0]] = i[1]

    for i in range(N-1):
        index = find(visit,node)
        print(index)
        for d in mapping[index]:
            if node[d[0]] > node[index]+d[1]:
                node[d[0]] = node[index] + d[1]
    node[start] = 0
    return node
  
s = solve(1) # 1 -> first, 1-> second
print(s)
fir = solve(first) # first -> second, first->end
print(fir)
sec =solve(second) # second -> first, second -> end

comp1 = s[second] + sec[first] + fir[N]
comp2 = s[first] + fir[second]+sec[N]

print(sec)
result = comp1 if comp1 < comp2 else comp2
if result >= INF:
    print(-1)
else:
    print(result)



