#Se creo una variable para ingresar la edad del usuario

Edad = int(input("ingresa tu edad: "))

if Edad <= 0: #Esta cadena de if, elif y else permite determinar el precio según la edad
    print("cantidad inválida")
elif Edad < 5:
    print("entrada gratis")
elif Edad <= 11:
    print("Debes pagar 5000")
elif Edad <= 59:
    print("Debe pagar 8000")
elif Edad >= 60:
    print("4000 por descuento de adulto mayor")