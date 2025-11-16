"""20. Aplicación “Inicio Seguro” – Intentos de inicio de sesión
Como usuario, quiero usar un while con máximo 3 intentos de contraseña.
Si acierto, mostrar “Acceso permitido”.
Si agoto los intentos, mostrar “Acceso denegado”."""

print("Inicio seguro")
contraseña = "Estiven123"
Maximo = 3
intento = 1

while intento <= Maximo:
    user = str(input("Ingresa la contraseña correcta para continuar: "))
    if contraseña == user:
        print("Puede ingresar")
        break
    else:
        print("contraseña incorrecta, vuelve a intentar: ")

    if intento == Maximo:
        print("No puedes seguir intentando ingresar")
    intento += 1
