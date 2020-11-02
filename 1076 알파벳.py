a=ord(input())

result = 0
data=[]
while True:
    data.append(chr(97+result))
    if 97+result == a:
        break
    result+=1
for i in data:
    print(i,end=" ")
