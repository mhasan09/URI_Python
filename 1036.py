import math
line=str(input())
split=line.split(" ")
a=float(split[0])
b=float(split[1])
c=float(split[2])
R1=(-b+math.sqrt((b*b)-(4*a*c)))/(2*a)
R2=(-b-math.sqrt((b*b)-(4*a*c)))/(2*a)

if(a<0 and b<0 and c<0):
    print("Impossivel calcular")

else:
    print("R1 = %.5f" %R1)
    print("R2 = %.5f" %R2)
