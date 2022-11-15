total=0
sueldo=0
sueldo=int(input("¿Cuanto cobras en una hora?: "))
trabajadores=0
trabajadores=(int)(input("¿Cuantos trabajadores hay?: "))
totaltrabajadores=0
contador=0
for x in range(1,7):
    numero2=0
    numero2=int(input("¿Cuantas horas hacen los trabajadores?: "))    
    contador=contador+1
    print("Los trabajadores han trabajado esto: ",totaltrabajadores)
    totaltrabajadores=totaltrabajadores+numero2



print("Los trabajadores han ganado: ",totaltrabajadores*sueldo)