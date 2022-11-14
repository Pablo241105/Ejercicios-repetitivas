total=0
contador=0
numero=0
for i in range(1,13):
    numero=int(input("Has ahorrado:"))
    total= total+numero
    contador=contador+1
    print("Hasta este mes:", contador,"llevas",total)
print("La cantidad que has ahorrado este año es de:", total)