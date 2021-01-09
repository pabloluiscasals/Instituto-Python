numeroSecreto = 777

print(
"""
+==================================+
| Bienvenido a mi juego, muggle!   |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")
numeroIngresado = int(input("ingrese un numero: "))
while numeroIngresado != numeroSecreto:
    print("¡Ja, ja! ¡Estás atrapado en mi ciclo!")
    numeroIngresado = int(input("ingrese un numero: "))
print("Bien hecho, muggle! Eres libre ahora")