'''
암호는 서로 다른 l개 알파벳
최소 1개의 모음
최소 2개의 자음 
암호는 증가하는 순서로 배열

조교들이 암호로 사용할 법함 문자 종류는 c가지
'''

L, C = map(int, input().split())

alphabet = input().split()
alphabet.sort()

moList = ['a','e','i','o', 'u']

class Data:
    def __init__(self):
        self.array = []
        self.length = 0
        self.ja =0
        self.mo = 0
    
    def add(self, inputData):
        if inputData in self.array:
            return False
        
        self.array.append(inputData)
        self.length += 1
        if inputData in moList:
            self.mo+=1
        else:
            self.ja+=1
        return True

    def pop(self):
        output = self.array.pop()
        self.length -= 1
        if output in moList:
            self.mo-=1
        else:
            self.ja-=1
            
    def result(self):
        if self.mo < 1 or self.ja < 2:
            return
        
        print(''.join(self.array))
 

def keyFunction(index, data):
    if data.length == L:
        data.result()
        return
    
    for i in range(index, len(alphabet)):
        if data.add(alphabet[i]):
            keyFunction(i+1, data)
            data.pop()

def solve():
    data = Data()
    keyFunction(0, data) 
solve()   
