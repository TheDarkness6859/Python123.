# El sistema debe mostrar siempre el menú principal hasta que el usuario seleccione salir. x
# Los productos deben almacenarse en una lista de diccionarios. x
# El menú debe manejar opciones inválidas sin cerrar el programa. x
# Se debe calcular y mostrar correctamente el valor total del inventario y el número total de productos. x
# El código debe estar modularizado en funciones, comentado y legible. x

def nombreP(): #Función que permite el ingreso del nombre del producto, con restricción de solo letras y sin espacios
     while True:
          Nombre = input("Nombre del producto: ").strip()

          if Nombre == "" or not Nombre.replace(" ", "").isalpha():
             print("el nombre no puede estar vacío ni tener números.")
             continue
          else:
               print(f"Nombre agregado correctamente: {Nombre}")
               return Nombre
    
def precio(): #Función que permite ingresar el precio del producto, limitado solo a números enteros y decimales
     while True:
          try:
               Precio = float(input(f"Ingresa el precio del producto: "))

               if Precio <= 0:
                    print("elige un número mayor a cero")
               else:
                    print(f"el precio del producto fue agregado correctamente")
               return Precio
          except ValueError:
               print("debes ingresar un número válido como 10.50 o 5")

def cantidad(): #Función que permite ingresar la cantidad de productos que se quieren agregar a el inventario
     while True:
          try:
               Cantidad = int(input(f"ingresa la cantidad de productos que deseas: "))

               if Cantidad <= 0:
                    print("elige un número mayor a cero")
               else:
                    print(f"cantidad de productos agregada correctamente al inventario")
                    return Cantidad
          except ValueError:
               print("Debes ingresar solo números enteros")
     return


def agregar(): #Una de las funciones principales, permite agrupar las funciones anteriores en una sola y agregar productos al diccionario e inventario
      global inventario
      while True:
          print("Ok, digita la siguiente información:") 
          print()
          nombre = nombreP() #Se llama a la función con ese nombre y se guarda su valor en una variable con similutud al dato ingresado
          print()
          Precio1 = precio() #Se llama a la función con ese nombre y se guarda su valor en una variable con similutud al dato ingresado
          print()
          Cantidad = cantidad() #Se llama a la función con ese nombre y se guarda su valor en una variable con similutud al dato ingresado
          print()
          costo_total = Precio1 * Cantidad #Se calcula el costo de los productos tomando el precio y la cantidad

          #Creación del diccionario que guarda cada elemento, tomandolos de las variables dadas por las funciones
          productoN ={"Nombre" : nombre,
                        "Precio" : Precio1,
                        "Cantidad" : Cantidad,   
                        "Total" : costo_total
                    }
            
          inventario.append(productoN) #Permite agregar al inventario el diccionario de cada producto ingresado y lo pone como nuevo elemento al final de el inventario
          print(f"producto: {nombre} agregado correctamente, el total de tu factura es:{costo_total}")
          
          while True: #Este bucle permite tomar la decisión de seguir agregando productos o terminar la función principal, este ciclo solo permite ingresar s o n
               continuar = input("Deseas continuar ingresando productos (s/n)").lower().strip()
               
               if continuar == "" or not continuar.replace(" ", "").isalpha():
                    print("el nombre no puede estar vacío ni tener números.")
                    continue
               elif continuar == "s":
                    break
               elif continuar == "n":
                    return
               else:
                    print("Ingrese (s/n)")   

#Otra de las funciones principales, esta permite interactuar con el inventario, para ver lo que hay en este o agregar nuevos productos directamente
def inv():
     global inventario
     while True:
          if not inventario: #Detecta si en el inventario no hay ningún producto
               print()
               print("No se han agregado productos")
               print()
          else: #Permite recorrer el inventario y poniendo al información agregada con anterioridad por el usuario
               for objeto in inventario:
                    print(f"| {objeto['Nombre']} | Cantidad: {objeto['Cantidad']} | Precio: ${objeto['Precio']:,.2f}")
                    print() 

          while True:                 
               acceso =input("quieres agregar productos? (s/n): ").strip().lower() #Esta variable permite ingesar una decisión, agregar productos directamente o no agregarlos, esta limitado solo para s o n
               print()
               if acceso == "" or not acceso.replace(" ", "").isalpha():
                    print("el nombre no puede estar vacío ni tener números.")
                    continue
               elif acceso == "s":
                    agregar()
               elif acceso == "n":
                    return
               else:
                    print("Ingrese (s/n)") 

#La ultima función principal, esta permite saber cuantos productos tenemos en el inventario y la sumatoria total de todos los productos
def calcular():
     global inventario #Permite a enterar al inventario fuera de una función
     if not inventario: #Detecta si hay productos en el inventario
               print("No se han agregado productos")
               return
     else:
          total = 0    #Permite iniciar el bucle e ir sumando el total de cada producto

          for objeto in inventario: #Recorre el inventario y va agregando el total de cada producto para irlo agregando a la variable con el mismo nombre
               total += objeto['Total']

          cantidad_Total = len(inventario) #Cuenta cuantos productos hay actualmente en el inventario y agrega el número restante a la variable
          
          print(f"La cantidad total de productos en el inventario es: {cantidad_Total} y la sumatoria de todos estos es: {total}")                       

inventario = [] #Crea el inventario (lista)

#Ccrea un bucle con todas las funciones y las condiciones para acceder a cada una de estas
while True:
     
     print("Bienvenido a Inventory s.a")
     print()
     print("1.añadir objeto al inventario")
     print("2.ver objeto del inventario")
     print("3.Analizar datos")
     print("4.Salir")
     print()

     try:
          Dec =int(input("¿Que quieres hacer?: ")) #Crea una variable que permite condicionar para tomar decisiones mas facil
          print()
          
          if Dec == 1: #Si se cumple permite llamar a la función agregar
               agregar()

          elif Dec == 2: #Si se cumple permite llamar a la función inv
               inv()

          elif Dec == 3: #Si se cumple permite llamar a la función calcular
               calcular()
               input("Presiona ENTER para volver al menú principal")

          elif Dec == 4: #Si se cumple termina el ciclo directamente y se acaba todo el proceso
               print("¡Gracias por usar Inventory S.A.! Saliendo del programa...")
               break
          else:
               print("valor ingresado incorrecto") #Detecta los valores incorrecto 
               input("Presiona ENTER para volver al menú principal") #Permite que el ciclo no se repita de inmediato y deje ver el mensaje
     except ValueError:
           print("Solo puedes ingresar números") #Detecta si se estan ingresando letras
           input("Presiona ENTER para volver al menú principal") #Permite que el ciclo no se repita de inmediato y deje ver el mensaje



                   


          


     








