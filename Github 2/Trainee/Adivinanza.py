"""9. Concurso “Adivina el número secreto”
Como participante, quiero que el programa me pida un número entre 1 y 5 usando un while.
Si acierto, mostrar “¡Correcto!”.
Si no, mostrar “Intenta otra vez” y seguir hasta acertar."""

print("Adivina el numero")

while True:
    datos=int(input("ingresa numero del 1 al 5:"))
    if datos == 3 :
        print("correcto")
        break
    else:
     print("intenta otra vez")