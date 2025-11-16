"""19. Tienda de helados – Registro de clientes atendidos
Como empleado, quiero usar un while que cuente clientes hasta que el número supere 15.
Si el número es múltiplo de 5, mostrar “Pausa para limpieza”.
Al final, mostrar “Turno finalizado”."""

clientes = 1

while clientes <= 15:
    print(f"Cliente numero : {clientes} atendido")
    if clientes % 5 == 0:
        print(f"Turno {clientes}, espere, Pausa para la limpieza")
    clientes += 1
    
print(f"Turno Finalizado")
