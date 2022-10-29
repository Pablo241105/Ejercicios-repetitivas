numeros=0
numeros=int(input("Cuantos numeros: "))
numerofinal=0
menor=0
mayor=0
cero=0
while numerofinal!=numeros:
    num=int(input("Estos son los resultados: "))
    if num<0:
        menor+=1
    if num>0:
        mayor+=1
    if num==0:
        cero+=1
    numerofinal+=1
print(mayor,"Estos son mayores que cero",menor,"Estos menores que cero ",cero,"Estos son cero")