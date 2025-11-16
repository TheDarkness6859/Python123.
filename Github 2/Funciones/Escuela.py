"""24. Escuela “Aprende con Funciones” – Promedio de notas
Como profesor, quiero crear una función promedioNotas() que reciba tres notas y calcule el promedio.
Si el promedio es mayor o igual a 3.0, mostrar “Aprobado”; si no, “Reprobado”."""

def promedioNotas(n1, n2, n3):
    promedio = (n1 + n2 + n3) / 3

    if promedio >= 3.0:
        print("Aprobado")
    else:
        print("Reprobado")

nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))

promedioNotas(nota1, nota2, nota3)