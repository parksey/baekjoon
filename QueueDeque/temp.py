N, K = map(int ,input().split())

friend = [str(i) for i in range(1,N+1)]
n = N
k = K-1

length = len(friend)
seq = 0

result = []
while friend:

    seq += k
    if seq+1 >= length:
        seq = (seq)%length
    length -= 1
    result.append(friend[seq])
    del friend[seq]
    
print('<'+', '.join(result)+'>')
