class Node():
    def __init__(self, x=-1):
        self.data =x
        self.link = None
        self.back = None
        self.size= 0
        
    def push(self, next_node):
        self.link = next_node
        next_node.back = self
    
head = tail = Node()
N, K = map(int, input().split())
for i in range(1,N+1):
    tail.push(Node(i))
    tail=tail.link
    head.size += 1

tail.link = head.link
head.link.back = tail
h = head.link
h_size = head.size
result = []
while h_size != 0:
    for i in range(K-1):
        h = h.link
    result.append(h.data) # 1 2 3 4 5 6 7 
    h.back.link = h.link
    h.link.back = h.back
    h = h.link
    h_size -= 1

print("<"+', '.join(map(str,result))+">")