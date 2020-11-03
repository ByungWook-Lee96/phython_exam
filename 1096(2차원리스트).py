

n=int(input())
array=[[0 for col in range(20)] for row in range(20)]
data=[0 for i in range(n)]
for i in range(n):
    data[i]=list(map(int,input().split()))
    array[data[i][0]-1][data[i][1]-1]=1

for i in range(19):
    for j in range(19):
        print(array[i][j],end=" ")
    print()


