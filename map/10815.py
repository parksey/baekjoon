N = int(input())

have = input().split()
have = set(have)
M = int(input())

check_list = input().split()

print(' '.join(map(lambda x: '1' if x in have else '0', check_list)))