"""5. Escuela “Aprende Más” – Registro de tareas entregadas
Como profesor, quiero usar un while que sume tareas hasta 10. Si el contador llega a 10, mostrar “¡Todas las tareas recibidas!”. Si aún no llega, mostrar cuántas faltan."""

tareas = 0

while tareas < 10:
    print("tareas registradas:", tareas)
    print("faltan:", 10 - tareas)
    tareas += 1 

print("todas las tareas recibidas.")
