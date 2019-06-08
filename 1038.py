p1=4.00
p2=4.50
p3=5.00
p4=2.00
p5=1.50

line=str(input())
split=line.split(" ")

y=int(split[0])
amount=int(split[1])

if(y==1):
    total = p1*amount
    print("Total: R$ %0.2f"%total)

elif(y==2):
    total = p2*amount
    print("Total: R$ %0.2f"%total)

elif(y==3):
    total = p3*amount
    print("Total: R$ %0.2f"%total)

elif(y==4):
    total = p4*amount
    print("Total: R$ %0.2f"%total)

elif(y==5):
    total = p5*amount
    print("Total: R$ %0.2f"%total)

