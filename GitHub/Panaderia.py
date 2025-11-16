comprar = int(input("Ingresa la cantidad de panes que quiere comprar: "))
Pan = 300
Descuento = Pan * comprar * 10 / 100
Descuento1 = Pan * comprar * 20 / 100

if comprar > 20:
    print(f"El total de tu compra con el 10% de descuento es: {Descuento}")
elif comprar > 50:
    print(f"El total de tu compra con el 20% de descuento es:{Descuento1}")
elif comprar < 0:
    print("cantidad invalida")
else:
    print(f"El total de tu compra es:{Pan * comprar}")