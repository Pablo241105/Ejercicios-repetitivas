import random
numero=random.randint(1,100)
fallos=1
nummero1=0
numero1=int(input("Di un numero:"))
while numero1!= numero and fallos<10:
    int(input("Dime otro numero:"))
if(numero1!=numero):
    fallos+1
if(fallos==10):
    print(numero)
if(fallos<10):
    print("Lo has conseguido")

