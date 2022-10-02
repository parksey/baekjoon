equation = input()

minusStart = False
number = ""
result = 0
for c in equation:
    if c >= '0' and c<='9':
        number += c
        continue
            
    if number:
        if minusStart:
            result -= int(number)
        else:
            result += int(number)
    
    if c == '-':
        minusStart = True
    number = ""
    
if minusStart:
    result -= int(number)
else:
    result += int(number)
print(result)
