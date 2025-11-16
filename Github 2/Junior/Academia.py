"""15. Academia “CodeStart” – Contador de ejercicios completados
Como estudiante, quiero usar un for del 1 al número que indique.
Si el número es múltiplo de 5, mostrar “¡Gran avance!”.
Si no, solo mostrar “Ejercicio X completado”."""

print("Bienvenido a la academia codestart")
numero = int(input("Ingresa la cantidad de ejercicios realizados: "))
for ejercicio in range(1,numero + 1):
    if ejercicio % 5 == 0:
        print(f"{ejercicio} completados,gran avance")
    else:
        print(f"Ejercicio {ejercicio} completado") 