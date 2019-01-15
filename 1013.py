line=str(input())
linea=line.split()
a=int(linea[0])
b=int(linea[1])
c=int(linea[2])
ab=(a+b+abs(a-b))/2
ac=(a+c+abs(a-c))/2
abc=(ab+ac+abs(ab-ac))/2
print('%d eh o maior'%abc)
