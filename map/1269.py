N, M = map(int ,input().split())

n_list = set(map(int,input().split()))
m_list = set(map(int, input().split()))

cnt = 0
for i in n_list:
    if i in m_list:
        cnt += 1

print(N+M-cnt*2)