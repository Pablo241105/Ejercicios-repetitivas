limiteinferior=0
limitesuperior=0
limiteinferior=(int)(input("Di el limite inferior: "))
limitesuperior=(int)(input("Di el limite superior: "))
while limiteinferior>limitesuperior:
    print("No se puede")
    limiteinferior=(int)(input("Di el limite inferior: "))
    limitesuperior=(int)(input("Di el limite superior: "))

numeros=0
numeros=(int)(input("Dime un numero: "))
suma=0
while numeros!=0:
  numeros=(int)(input("Dime un numero: "))
  suma=numeros+suma

print("La suma de tus numeros es:", suma)