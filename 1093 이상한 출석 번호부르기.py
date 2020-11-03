n=int(input())
data=list(map(int,input().split()))
data1=[0 for i in range(23)]
for i in range(n):
    data1[data[i]-1]+=1
for i in data1:
    print(i,end=" ")
