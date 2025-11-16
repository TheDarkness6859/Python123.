"""Programa que permite agregar productos a un inventario. x
El programa debe solicitar tres datos obligatorios: nombre, precio y cantidad. x
Si el usuario ingresa un valor inválido en precio o cantidad, el sistema debe mostrar un mensaje de error y pedir nuevamente el dato. x
El cálculo del costo total debe realizarse correctamente y mostrarse de forma clara. x
El código debe estar estructurado, comentado y sin errores de sintaxis. x
"""


print("Bienvenido a Inventory s.a")
print("1.añadir objeto al inventario")
#print("2.ver objeto del inventario") implementación futura 


while True: #ciclo que permite repetir la pregunta si no se cumple la condición de la variable (Dec)
    try: #permite controlar codigo problematico, como escribir un número en un string
      Dec =int(input("¿Que quieres hacer?: "))
      if Dec == 1:
             print("ok, digita la siguiente información:")
             break #termina el ciclo al responder lo necesario o pedido
      else:
            print(" Error, elige una opción correcta")
    except ValueError: #Permite detectar errores si no se cumple la restriccion de números enteros
        print("debe escribir un número")
        
while True: #ciclo que permite repetir la pregunta si no se cumple la condición de la variable (Nombre)
          Nombre = input("Nombre del producto: ").strip() #detecta el nombre del producto y quita los espacos del inicio y final
          if Nombre == "" or not Nombre.replace(" ", "").isalpha(): #detecta si la palabra no fue ingresada o si tiene números
             print("el nombre no puede estar vacío ni tener números.")
             continue #permite continuar el ciclo
          else:
                print(f"Nombre agregado correctamente: {Nombre}")
                break #termina el ciclo al responder lo necesario o pedido

while True: #ciclo que permite repetir la pregunta si no se cumple la condición de la variable (Precio)
     try: #permite controlar codigo problematico, como escribir un número en un string
          Precio = float(input(f"Ingresa el precio del articúlo {Nombre}: ")) #permite ingresar números flotantes(decimales o enteros)
          if Precio <= 0:
               print("elige un número mayor a cero")
          else:
               print(f"el precio de {Nombre} fue agregado correctamente")
               break #termina el ciclo al responder lo necesario o pedido
     except ValueError: #Permite detectar errores si no se cumple la restriccion de números enteros o decimales
          print("debes ingresar un número válido como 10.50 o 5")

while True:
     try: #permite controlar codigo problematico, como escribir un número en un string
          Cantidad = int(input(f"ingresa la cantidad de articulos de {Nombre} que deseas: "))
          if Cantidad <= 0:
               print("elige un número mayor a cero")
          else:
               print(f"cantidad de articulos  de {Nombre} agregada correctamente al inventario")
               break #termina el ciclo al responder lo necesario o pedido
     except ValueError: #Permite detectar errores si no se cumple la restriccion de números enteros
          print("Debes ingresar solo números enteros")

costo_total = Precio * Cantidad #calcula los datos brindados por los usuarios
print("Gracias por digitar tus datos, tú factúra es la siguiente")
print(f"Producto: {Nombre} | Precio: {Precio} | Cantidad: {Cantidad} | Total: {costo_total}")