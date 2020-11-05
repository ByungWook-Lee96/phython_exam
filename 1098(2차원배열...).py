h,w=map(int,input().split())
n=int(input())
data=[[0 for i in range(4)]for j in range(n)]
for i in range(n):
    data[i]=list(map(int,input().split()))

lis=[[0 for _ in range(w)]for _ in range(h)]
start=[data[0][2]-1,data[0][3]-1]
i=0
while i<n:
    lis[data[i][2]-1][data[i][3]-1]=1
    x = data[i][0]
    if data[i][1]==0:
        for j in range(x):
            lis[data[i][2] - 1][data[i][3] - 1+j]=1
    else :
        for j in range(x):
            lis[data[i][2] - 1+j][data[i][3] - 1] = 1
    i+=1


for i in range(h):
    for j in range(w):
        print(lis[i][j],end=" ")
    print()



