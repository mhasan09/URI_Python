y= float(input())
if(y>=0 and y<=25):
    print("Intervalo [0,25]")
elif(y>25 and y<=50):
    print("Intervalo (25,50]")
elif(y>50 and y<=75):
    print("Intervalo (50,75]")
elif(y>75 and y<=100):
    print("Intervalo (75,100]")
elif(y<0 or y>100):
    print("Fora de intervalo")