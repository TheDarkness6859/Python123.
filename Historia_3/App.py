from Servicio import *

def Menu():
    while True:
        
        print("Bienvenido a Inventory s.a")
        print()
        print("1.añadir objeto al inventario")
        print("2.ver objeto del inventario")
        print("3.Analizar datos")
        print("4.Buscar producto")
        print("5.Actualizar producto")
        print("6.Eliminar producto")
        print("7.Guardar json")
        print("8.Exportar csv")
        print("9.cargar csv")
        print("10.Fin")
        print()

        try:
            Dec = int(input("¿Que quieres hacer?: "))
            print()
            
            if Dec == 1:
                agregar()

            elif Dec == 2:
                inv(Inventario)

            elif Dec == 3:
                estadisticas(Inventario)
                input("Presiona ENTER para volver al menú principal")
            
            elif Dec == 4:
                Buscar(Inventario)
                input("Presiona ENTER para volver al menú principal")

            elif Dec == 5:
                Actualizar(Inventario)
                input("Presiona ENTER para volver al menú principal")

            elif Dec == 6:
                eliminar(Inventario)

            elif Dec == 7:
                guardarJSON()
                input("Presiona ENTER para volver al menú principal")
            
            elif Dec == 8:
                exportarCSV()
                input("Presiona ENTER para volver al menú principal")
            
            elif Dec == 9:
                cargarCSV()
                input("Presiona ENTER para volver al menú principal")

            elif Dec == 10:
                print("¡Gracias por usar Inventory S.A.! Saliendo del programa...")
                break 
            else:
                print("valor ingresado incorrecto")
                input("Presiona ENTER para volver al menú principal")                           
        except ValueError:
            print("Solo puedes ingresar números")
            input("Presiona ENTER para volver al menú principal")

Menu()

