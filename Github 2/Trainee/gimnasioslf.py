"""3. Gimnasio “Solo Leveling Fit” – Motivación diaria
Como entrenador, quiero usar un while que repita 5 veces el mensaje “¡Tú puedes lograrlo!”, pero en la última repetición muestre “¡Excelente trabajo, terminaste!”."""

frase= "tu puedes lograrlo "
contador = 5

while contador <= 5:
    print(frase)
    contador -= 1 
    if contador == 1:
        print("excelente trabajo terminaste")
        break 