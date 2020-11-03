n=int(input())
data=list(map(int,input().split()))
min=9999999
for i in data:
    if min > i:
        min=i
print(min)