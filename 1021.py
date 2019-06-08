y=float(input())
x=float('%.2f'%y)
a=x//100
b=x%100
c=b//50
d=b%50
e=d//20
f=d%20
g=f//10
h=f%10
i=h//5
j=h%5
k=j//2
l=j%2
m=l//1
n=l%1
o=n//0.50
p=n%0.50
q=p//0.25
r=p%0.25
s=r//0.10
t=r%0.10
u=t//0.05
v=t%0.05
v1=v//0.01
v2=v%0.01

print("NOTAS:")
print('%1.0f nota(s) de R$ 100.00'%a)
print('%1.0f nota(s) de R$ 50.00'%c)
print('%1.0f nota(s) de R$ 20.00'%e)
print('%1.0f nota(s) de R$ 10.00'%g)
print('%1.0f nota(s) de R$ 5.00'%i)
print('%1.0f nota(s) de R$ 2.00'%k)
print("MOEDAS:")
print('%1.0f moeda(s) de R$ 1.00'%m)
print('%1.0f moeda(s) de R$ 0.50'%o)
print('%1.0f moeda(s) de R$ 0.25'%q)
print('%1.0f moeda(s) de R$ 0.10'%s)
print('%1.0f moeda(s) de R$ 0.05'%u)
print('%1.0f moeda(s) de R$ 0.01'%v1)


