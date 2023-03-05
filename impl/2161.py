'''
N장의 카드
1~N 까지의 번호

1. 제일 위에 있는 카드를 바닥에 버린다.
2. 제일 위에 있는 카드를 제일 아래에 이쓴ㄴ 카드 밑으로 옮긴다.
'''
from collections import deque
N = int(input())

nList = [i for i in range(1,N+1)]

queue = deque(nList)
size = len(queue)
leftStack = []
while size > 1:
    leftStack.append(queue.popleft())
    queue.append(queue.popleft())
    size -= 1
leftStack.append(queue.popleft())
print(*leftStack)