
total=0
contador=0

for x in range(1,13):
    numero=int(input("Dime cuanto este mes: "))
    total=total+numero
    contador=contador+1
    print("Hasta este mes: ", contador,"Has ahorrado: ", total)
print("En total a lo largo del año has ahorrado: ", total)

