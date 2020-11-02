a=int(input())
start=0
sum=0
while start <= a:
    if start % 2 == 0:
        sum+=start
    start+=1
print(sum)