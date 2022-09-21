from collections import deque


K = int(input())

def find(start, line, v_list):
    v_list[start] = 1
    isFirst = False
    
    queue = deque([start])
    
    while queue:
        left = queue.popleft()
        team = 2 if v_list[left] == 1 else 1
        
        for d in line[left]:
            if v_list[d] == 0:
                v_list[d] = team
                queue.append(d)
            elif v_list[d] != team:
                return False
    return True
            

def solve(V,E):
    v_list = [0]*(V+1)
    line =[[] for i in range(V+1)]
    
    for _ in range(E):
        s,e = map(int,input().split())
        line[s].append(e)
        line[e].append(s)

    for i in range(1,V+1):
        if v_list[i] == 0:
            if not find(i, line, v_list):
                return False
    return True



for i in range(K):
    V,E = map(int, input().split())
    
    if solve(V,E):
        print("YES")
    else:
        print("NO")


    