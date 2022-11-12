numero = (int)(input("Dime un número:\n"))
contador = 0

for x in range(2, numero):
    if numero%x==0:
        contador +=1
if contador >= 1:
    print("No es ")
else:
    print("Es primo")