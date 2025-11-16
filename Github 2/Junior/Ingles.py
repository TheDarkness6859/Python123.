"""18. Academia de inglés – Repetición de palabras
Como estudiante, quiero ingresar una palabra y usar un for para repetirla 5 veces.
Si el contador es impar, mostrar la palabra en minúsculas.
Si es par, mostrarla en mayúsculas."""

print("Bienvenido a la academia de inglés")

Palabra = str(input("dime tu palabra: "))

for repetir in range(1, 5 + 1 ):
    if repetir % 2 == 0:
        print(f"{repetir}: {Palabra.upper()}")
    else:
        print(f"{repetir}: {Palabra.lower()}")