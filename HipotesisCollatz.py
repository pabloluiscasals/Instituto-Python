cO = int(input("Ingrese un numero entero que no sea negativo ni cero: "))
contador = 0
while cO != 1:
    contador += 1
    if cO % 2 == 0:
        cO = cO / 2
        print (cO)
    else:
        cO = 3 * cO + 1
        print (cO)
print (contador)