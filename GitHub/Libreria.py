Libro = 25000

print("Bienvenido a la libreria El Saber")
Compra = int(input("¿Cuantos libros quieres comprar? "))
Total = Libro * Compra
Estudiante = Libro * Compra * 0.15
if Compra <= 0:
    print("Cantidad invalida")
elif Compra > 0:
    Persona = str(input("¿Eres un estudiante?")).lower()
    if Persona == "si":
        cupon = str(input("¿Tienes cupon?"))
        if cupon == "si":
            cupon1 = str(input("Ingresa tu cupon: ")) 
            if cupon1 == "CUPON10":
                print(f"El total de tu compra con descuento es:{Estudiante * 0.10}")
            else:
                print(f"cupon invalido, el total de tu compra es:{Estudiante}")
        else:
            print(f"el total de tu compra es:{Estudiante}")
    else:
        print(f"el total de tu compra es:{Total}")
else:
    print(f"el total de tu compra es:{Total}")







