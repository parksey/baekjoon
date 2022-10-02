N  = int(input())
result = [list(map(int, input().split())) for _ in range(N)]

result.sort(key=lambda x: (x[1], x[0]))

cnt = 1
end = result[0][1]
for i in range(1,N):
    if result[i][0] >= end:
        cnt += 1
        end = result[i][1]
print(cnt)