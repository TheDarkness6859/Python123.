"""17. Panadería “Don Pancho” – Producción diaria
Como panadero, quiero usar un for del 1 al 12.
Si el número es 6, mostrar “Mitad de la producción completada”.
Si es 12, mostrar “¡Día finalizado!”."""

for numero in range(1, 13):  
    if numero == 6:
        print(f"Producción {numero} - Mitad de la producción completada")
    elif numero == 12:
        print(f"Producción {numero} - ¡Día finalizado!")
    else:
        print(f"Producción {numero}")