# agregar_producto(inventario, nombre, precio, cantidad) x
# mostrar_inventario(inventario) x
# buscar_producto(inventario, nombre) → retorna el dict o None 
# actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None)
# eliminar_producto(inventario, nombre)
# calcular_estadisticas(inventario) → retorna tupla/dict con métricas

import json
import csv

Inventario = []

ARCHIVO_JSON = "/home/thedarkness6859/Documentos/Riwi Semana 1/vsc/Python 1 month/Historia de usuario/Historia 3/Inventario.json"
ARCHIVO_CSV = "/home/thedarkness6859/Documentos/Riwi Semana 1/vsc/Python 1 month/Historia de usuario/Historia 3/Inventario.csv"

# ---Guardar en JSON---

def guardarJSON():
    with open(ARCHIVO_JSON, "w") as archivo:
        json.dump(Inventario, archivo, indent=4)
    print("\n[OK] Datos guardados en Inventario.json\n")

#---Cargar desde JSON---

def cargarJSON():
    try:
        with open(ARCHIVO_JSON, "r") as archivo:
            datos = json.load(archivo)
            return datos
    except FileNotFoundError:
        return []   # si no existe, lista vacía

#---Exportar a CSV---

def exportarCSV():
    with open(ARCHIVO_CSV, "a", newline="") as archivo:
        writer = csv.writer(archivo)
        writer.writerow(["Nombre","Precio","Cantidad","Total"])  # encabezados
        for est in Inventario:
            writer.writerow([est["Nombre"], est["Precio"], est["Cantidad"], est["Total"]])

    print("\n[OK] Datos exportados a Inventario.csv\n")

#---Funcion de agregar productos---
def agregar():
      global Inventario
      while True:
          print("Ok, digita la siguiente información:") 
          print()
          nombre = nombreP()
          print()
          Precio1 = precio()
          print()
          Cantidad = cantidad()
          print()
          costo_total = Precio1 * Cantidad

          productoN ={"Nombre" : nombre,
                        "Precio" : Precio1,
                        "Cantidad" : Cantidad,   
                        "Total" : costo_total
                    }
            
          Inventario.append(productoN)
          print(f"producto: {nombre} agregado correctamente, el total de tu factura es:{costo_total}")
          
          while True:
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

def nombreP():
     while True:
          Nombre = input("Nombre del producto: ").strip()

          if Nombre == "" or not Nombre.replace(" ", "").isalpha():
             print("el nombre no puede estar vacío ni tener números.")
             continue
          else:
               print(f"Nombre agregado correctamente: {Nombre}")
               return Nombre
    
def precio():
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

def cantidad():
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
#---Final función agregar---

#---Función inventario---
def inv(Inventario):
     while True:
          if not Inventario:
               print("\n No se han agregado productos")
          else:
               for objeto in Inventario:
                    print(f"|Nombre: {objeto['Nombre']}| Precio: {objeto['Precio']}| Cantidad: ${objeto['Cantidad']:,.2f}")

          while True:                 
               acceso =input("quieres agregar productos? (s/n): ").strip().lower()
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
#---Fin de la función inventario---

#---Función calcular---
def estadisticas(Inventario):
    if not Inventario:
        print("\n No hay productos en el inventario.\n")
        return

    unidades_totales = sum(prod["Cantidad"] for prod in Inventario)
    valor_total = sum(prod["Cantidad"] * prod["Precio"] for prod in Inventario)
    #Indica cómo seleccionar el valor que se comparará. y lambda es Indica que, para cada producto, use su "Cantidad" para comparar
    producto_mas_caro = max(Inventario, key=lambda p: p["Precio"])
    producto_mayor_stock = max(Inventario, key=lambda p: p["Cantidad"])

    print("\nESTADÍSTICAS DEL INVENTARIO")
    print(f"Unidades totales: {unidades_totales}")
    print(f"Valor total del inventario: ${valor_total:,.2f}")
    print(f"Producto más caro: {producto_mas_caro['Nombre']} (${producto_mas_caro['Precio']})")
    print(f"Producto con mayor stock: {producto_mayor_stock['Nombre']} ({producto_mayor_stock['Cantidad']} unidades)")
#---Fin de la función calcular---

#---Función buscar---
def Buscar(Inventario):
    if not Inventario:
        print("No hay productos para actualizar.")
        return

    buscar = str(input("Ingrese el NOMBRE del PRODUCTO: "))
    
    for Pro in Inventario:
        if Pro["Nombre"] == buscar:
            print(f"Estudiante encontrado: {Pro}")
            break
#---Fin de función buscar---

#---Función actualizar---
def Actualizar(Inventario):
    if not Inventario:
        print("No hay productos para actualizar.")
        return

    Buscar = str(input("Ingrese el NOMBRE del producto a actualizar: "))

    encontrado = False
    for Pro in Inventario:
        if Pro["Nombre"] == Buscar:
            
          encontrado = True
          print(f"Producto encontrado: {Pro}")
            
            # Nuevos datos
          while True:
               nombre = str(input("Ingrese el nuevo nombre: "))
               if nombre == "" or not nombre.replace(" ", "").isalpha():
                    print("el nombre no puede estar vacío ni tener números.")
                    continue
               else:
                    break

          while True:
                    try:
                         cantidad = int(input("Ingrese la nueva cantidad: "))
                         if cantidad <= 0:
                              print("Valor incorrecto")
                              continue
                         else:
                              break
                    except ValueError:
                         print("Solo puedes comprar cantidades exactas")

          while True:
                    try:
                         precio = float(input("Ingrese el precio nuevo: "))
                         if precio <= 0:
                              print("Valor incorrecto")
                              continue
                         else:
                              break
                    except ValueError:
                         print("Solo puedes comprar cantidades exactas")
                         continue

          Pro["Nombre"] = nombre
          Pro["Cantidad"] = cantidad
          Pro["Precio"] = precio

          print("\n Producto actualizado correctamente:")
          print(Pro)
          break
    if not encontrado:
          print("No existe un producto con ese NOMBRE.")
#---Fin de función actualizar---

#---Función eliminar---
def eliminar(Inventario):
    if not Inventario:
        print("No hay productos para eliminar.")
        return
    
    while True:
     try:
          Prod = str(input("Ingrese el nombre del estudiante a eliminar: "))
          if Prod == "" or not Prod.replace(" ", "").isalpha():
               print("el nombre no puede estar vacío ni tener números.")
               continue
          else:
               break
     except ValueError:
          print("Debe ingresar un nombre valido.")

    encontrado = False
    for Pro in Inventario:
        if Pro["Nombre"] == Prod:
            encontrado = True
            print(f"Producto encontrado: {Pro}")

            confirmacion = input("¿Está seguro que desea eliminarlo? (s/n): ")

            if confirmacion.lower() == 's':
                Inventario.remove(Pro)
                print("Producto eliminado correctamente.")
            else:
                print(" Operación cancelada.")
            break

    if not encontrado:
        print("No existe ningún producto con ese nombre.")





        