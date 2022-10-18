'''
Descripción: Ciclo While
Autor: Jessica Castillo
Fecha: 27 de Septiembre 2022
'''
secret_number = 777

print(
"""
+==================================+
| ¡Bienvenido a mi juego, muggle!  |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")
num=int(input("Ingresa tu número"))

while secret_number !=num:
    print("¡Ja, ja! ¡Estás atrapado en mi bucle!" )
    print(
    """
    +==================================+
    | ¡Bienvenido a mi juego, muggle!  |
    | Introduce un número entero       |
    | y adivina qué número he          |
    | elegido para ti.                 |
    | Entonces,                        |
    | ¿Cuál es el número secreto?      |
    +==================================+
    """)
    num=int(input("Ingresa tu número"))

print("¡Bien hecho, muggle! Eres libre ahora")

