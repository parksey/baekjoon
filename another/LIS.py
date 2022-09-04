lis = [3,2,1,7,5,4,2,6]

def find(end):
    max =0 
    for i in range(8):
        data = [lis[i]]
        for j in range(i+1,8):
            if data[-1] < lis[j]:
                data.append(lis[j])
        print(data)
        if max < len(data):
            max = len(data)
    print(max)
find(0)