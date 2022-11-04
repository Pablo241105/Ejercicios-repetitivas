

def potencia(base, exponente):
    elevado= 1
    for x in range(exponente ):
        elevado = elevado * base
    return elevado


numero1=0
numero2=0
numero1=(int)(input("Di un numero: "))
numero2=(int)(input("Di otro numero: "))
#resultado = potencia(numero1,numero2)
print("La potencia es ", potencia(numero1,numero2))
