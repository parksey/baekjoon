T = int(input())
INF = 999999999
def find(weight, visit):
    min = INF
    index = 0
    for i in range(1,len(weight)):
        if visit[i]: continue
        
        if weight[i] < min:
            min = weight[i]
            index = i
    return index

def algo(line_map, s):
    
    length = len(line_map)
    weight = [INF]*length
    weight[s] = 0
    visit = [0]*length
    for i in range(1, length):
        index = find(weight, visit)
        visit[index] = 1
        for j in line_map[index]:

            if weight[j[0]] > weight[index] + j[1]:
                weight[j[0]] = weight[index] + j[1]
    return weight

def solve():
    t_list=[]
    
    n, m, t = map(int, input().split()) # 교차로, 도로, 목적지
    #6 9 2
    s, g, h = map(int, input().split())
    #2 3 1
    line_map = [[] for i in range(n+1)]
    
    for i in range(m):
        a,b,d = map(int, input().split())
        
        line_map[a].append([b,d])
        line_map[b].append([a,d])
        
    gh = 0
    for i in line_map[g]:
        if i[0] == h:
            gh = i[1]
            break
    
    start_list = algo(line_map, s)
    s2gh = start_list[g] + gh
    s2hg = start_list[h] + gh

    result = []
    for i in range(t):
        t_data = int(input()) 
        
        min_data =min(s2gh + algo(line_map, h)[t_data], s2hg + algo(line_map, g)[t_data])
        if min_data <= start_list[t_data]:
            result.append(min_data)
    return sorted(result) 


for i in range(T):
    print(*solve())
    

    
    