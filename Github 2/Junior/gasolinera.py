"""16. Gasolinera “LoopFuel” – Control de litros vendidos
Como operador, quiero usar un while que sume litros hasta superar 100.
Cada vez que se venda una cantidad, verificar:

Si el total aún es menor que 100 → mostrar “Sigue vendiendo”.
Si llega o supera 100 → mostrar “Meta diaria alcanzada”."""

print("Bienvenido a la gasolinera loopfuel")

gasolina = 1

while gasolina <= 100:
    if gasolina < 100:
        print(f"{gasolina} litros de gasolina Sigue vendiendo")
    else:
        print(f"{gasolina} litros de gasolina vendidos, meta diaria alcanzada")
    gasolina += 1