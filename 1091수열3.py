a,m,d,n=map(int,input().split())

#n-1번째
pre_num=a
for i in range(1,n):
    pre_num=(pre_num)*m+d

print(pre_num)