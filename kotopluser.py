import sys

stroka = sys.argv[1]

a = []
i = 0
while i <= len(stroka):
    
    a.append(stroka[i:i+1:1])
    i = i+1

result = 0
stroka_len = len(stroka)

for z in range(0, stroka_len):
    result = result + int(a[z])
    
print(result)