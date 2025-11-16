print("Elige un número")
print("1. para días en el gimnasio")
print("2. para ver tus puntos")
Tabla = int(input("Escoge: "))

if Tabla == 1:
    Dias = int(input("¿Cuántos días llevas entrenando?"))
    if Dias >= 4:
        print(f"¡Excelente disciplina! +1 punto de energía")
    elif Dias > 2:
        print("Bien, pero puedes dar más")
    elif Dias > 0:
        print("No aflojes, tú puedes mejorar")
    else:
        print("¿Qué esperas para venir?")

if Tabla == 2:
    Dias = int(input("¿Cuántos días llevas entrenando?"))
    if Dias >= 4:
        Energia = Dias // 4 
        print(f"Tu energía es: {Energia}")
    else:
        print("No tienes puntos")