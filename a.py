numero = (int)(input("Dime un número, pulsa el 0 para salir:\n"))
sumanumeros = 0
media = 0
while numero != 0:
    sumanumeros = sumanumeros + numero
    media = media + 1
    numero = (int)(input("Dime otro número, pulsa 0 para salir:\n"))

print("La suma de todos lo números es:", sumanumeros)
print("La media de todos los números es:", sumanumeros/media)