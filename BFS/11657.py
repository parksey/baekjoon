N,M = 500,500#map(int,input().split())
INF = 9999999999

v = [INF] * (N+1)
node_map = [[] for i in range(N+1)]

for i in range(1,500):
    s,e,a = i,i+1,-10000 #map(int,input().split())
    node_map[s].append([e,a])

def find(visit):
    min = INF
    index = 0
    for i in range(1, N+1):
        if min > v[i] and not visit[i]:
            index = i
            min = v[i]
    return index

def solve(sec, visit):
    if sec ==0:
        v[1] = 0
   
    for i in range(N):
        index = find(visit)
        visit[index] = 1
      
        for d in node_map[index]:
            if v[d[0]] > v[index]+d[1]:
                if sec:
                    return -1
                v[d[0]] = v[index] + d[1]
    return 0 
   
def main():
    for sec in range(2):    
        visit = [0] * (N+1)   
          
        if solve(sec, visit) == -1:
            return -1

if main() == -1:
    print(-1)
else:
    for i in v[2:]:
        if i == INF:
            print(-1)
        else:
            print(i)