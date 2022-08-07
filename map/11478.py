string = input()

result = set()
length = len(string)
def find(i):
    if i > length:
        return

    start = 0
    end = i
    while(end <= length):
        if string[start:end] not in result:
            result.add(string[start:end])
        start+=1
        end +=1
    
    find(i+1)
        
find(1)
print(len(result))