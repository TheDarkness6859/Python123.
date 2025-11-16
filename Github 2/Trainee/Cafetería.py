"""1. Cafetería “Buen Café” – Control de tazas servidas
Como barista, quiero usar un bucle for para mostrar cuántas tazas he servido del 1 al 10, pero si el número es 5, mostrar el mensaje “¡Mitad del turno completada!”."""

print("Bienvenido a la cafetería buen cafe")
print("Hoy voy a servir 10 tazas")

for i in range(1,11):
    print(i)
    if i == 5:
        print("Mitad del turno completado")

print("Muchas gracias por venir")