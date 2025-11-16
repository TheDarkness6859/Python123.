"""Academia de baile – Calentamiento previo
Como instructor, quiero usar un while para contar del 1 al 5.
Si el número es menor que 5, mostrar “Sigue calentando...”, y si llega a 5, mostrar “¡Listo para bailar!”."""

Contador = 1
Frase = "Sigue calentando..."
while Contador <= 5:
    print(Contador,Frase)
    Contador += 1 
    if Contador == 5:
        print("Listo para bailar")
        break 