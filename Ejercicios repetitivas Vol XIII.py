total=0
contador=1
sueldo=0
sueldo=int(input("¿Cuanto cobras en una hora?: "))
for x in range(1,7):
    numero=0
    numero=int(input(f"Dime cuantas horas has trabajado el dia {contador}:"))
    contador=contador+1
    total=total+numero
print("Has echado estas horas: ", total)
print("Esta semana has ganado: ", total*sueldo)