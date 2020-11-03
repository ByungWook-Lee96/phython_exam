n=int(input())
data=list(map(int,input().split()))
data.reverse()
for i in range(n):
    print(data[i],end=" ")
