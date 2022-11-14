contador=1
total=0
sueldo=0
sueldo=int(input("¿Cuanto cobras en una hora?: "))
trabajadores=0
trabajadores=(int)(input("¿Cuantos trabajadores hay?: "))
totaltrabajadores=0
for x in range(1,7):
    numero=0
    numero=int(input("Dime cuantas horas has trabajado el dia :"))
    contador=contador+1
    total=total+numero

    numero2=0
    numero2=int(input("¿Cuantas horas hacen los trabajadores?: "))    
    contador=contador+1
    contador=contador*trabajadores
    print("Los trabajadores han trabajado esto: ",totaltrabajadores)
    totaltrabajadores=totaltrabajadores+numero2
        

print("Has echado estas horas: ", total)
print("Esta semana has ganado: ", total*sueldo)
print("Los trabajadores han ganado: ",totaltrabajadores*sueldo)