numero = int(input("Introduce un número para comprobar si es primo:"))
for num in range(2, numero):
    
    if numero % num == 0:
        print("Es primo")
        else:
            print("No es")

