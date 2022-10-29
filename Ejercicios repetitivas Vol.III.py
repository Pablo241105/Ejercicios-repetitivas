numeros=0
numeros=(int)(input("Dime un numero: "))
suma=0
medianum=0
while numeros!=0:
  numeros=(int)(input("Dime un numero: "))
  suma=numeros+suma
  medianum=medianum+1

print("La suma de tus numeros es:", suma)
print("La media de tus numeros es:", suma/medianum)