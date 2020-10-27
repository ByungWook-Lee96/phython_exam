a,b,c=input().split(".")
if len(a)==3:
    a="0"+a
elif len(a)==2:
    a="00"+a
elif len(a)==1:
    a="000"+a
elif len(a) == 0:
    a = "0000" + a
if len(b)<2:
    b="0"+b
if len(c)<2:
    c="0"+c
print(a+"."+b+"."+c)