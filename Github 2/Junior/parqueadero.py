"""13. Parqueadero “AutoLoop” – Control de vehículos
Como vigilante, quiero usar un while que cuente vehículos hasta llegar a 20.
Si entra un número par, mostrar “Vehículo par registrado”.
Si el total llega a 20, mostrar “Capacidad completa”."""

print("Bienvenido al parqueadero autoloop")
maxima = 20
carros = 1
while carros <= maxima:

    if carros == maxima:
        print("capacidad completa")
    elif carros % 2 == 0:
        print(f"Vehículo {carros} par registrado")
    else:
        print(f"Vehículo {carros} registrado")
    carros += 1


        

        

