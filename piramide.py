bloques = int(input("Ingrese el número de bloques:"))
altura = 0
while bloques >0:#
    altura += 1 # Escribe tu código aquí.
    bloques = bloques - altura #
    if bloques < 0:
        altura = altura - 1
print("La altura de la pirámide:", altura)