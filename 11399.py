N = int(input())

data = sorted(list(map(int, input().split())))

result = 0
sum = 0
for d in data:
    sum += d
    result += sum
print(result)