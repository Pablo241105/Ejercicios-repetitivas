numero1=0
numero2=0
numero1=(int)(input("Dime un numero: "))
numero2=(int)(input("Dime otro numero: "))
par=0
for numero in range(numero1,numero2) :
    if numero % 2==0:
       par=par+1 
    else: 
      par=par+0
print(par+1)


