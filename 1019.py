x=int(input())
a=x//3600
b=x%3600
c=b//60
d=b%60
e=d//60
f=d%60

print('%d:%d:%d' %(a,c,f))
