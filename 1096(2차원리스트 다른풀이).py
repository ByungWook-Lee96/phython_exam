n=int(input())
array=[[0 for col in range(20)] for row in range(20)]
for i in range(n):
    b,c=map(int,input().split())
    array[b-1][c-1]=1

for i in range(19):
    for j in range(19):
        print(array[i][j],end=" ")
    print()


