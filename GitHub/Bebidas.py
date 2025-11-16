#Defini tres principales, con valores necesario para el ejercicio.

menu = 12.000 
Bebida = 3.000
iva = 0.08

#Imprimi bienvenida, pregunta y una opción elegible por el usuario.

print("Bienvenidos a los sabores de colombia")
print("quieres almorazar?")
opcion = str(input("(si/no): ")).lower()

#Aplique condiciones segun lo ingresado por el usuario para satisfacer cada necesidad

if opcion == "si": #Este if satisface a una respuesta, esta genera una cadena con otro if para realizar calcúlos
    print("nuestros almuerzos cuestan 12 mil, quieres acompañarlo con una bebida")
    aco = str(input("si/no")).lower()
    if aco == "si":
        print(f"el total de tu compra es: {menu + Bebida *(1 + iva)}")
    else:
        print(menu * (1 + iva))
elif opcion != "no": #Este elif permite crear una condición, la cual identifica si el usuario ingreso lo pedido
    print("Responde si o no porfavor")
else: #Este else permite que sino se cumple lo anterior arroje un mensaje
    print("esta bien, que tengas un gran dia")
