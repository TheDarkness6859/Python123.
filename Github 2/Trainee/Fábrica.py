"""6. Fábrica “LoopTech” – Control de producción
Como supervisor, quiero que un for muestre los productos fabricados del 1 al número que indique el usuario.
Si el número es par, mostrar “Producto verificado”.
Si es impar, mostrar “Producto pendiente”."""

fabrica = int(input("ingresa número de productos: "))
for i in range(1,fabrica + 1):
    if i % 2 == 0:
        print("Producto verificado")
    else:
        print("Producto pendiente")
