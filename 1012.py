linea=str(input())
linesplit=linea.split()
a=float(linesplit[0])
b=float(linesplit[1])
c=float(linesplit[2])
pi=3.14159
tri=(1/2)*a*c
cir=pi*pow(c,2)
trap=((a+b)/2)*c
sq=pow(b,2)
rec=a*b
print('TRIANGULO: %0.3f'%tri)
print('CIRCULO: %0.3f'%cir)
print('TRAPEZIO: %0.3f'%trap)
print('QUADRADO: %0.3f'%sq)
print('RETANGULO: %0.3f'%rec)