print("Bienvenido al parqueadero RapidCar")
horas = int(input("Ingresa las horas que permaneciste en el parqueadero: "))
costo_hora = 2000
if horas < 0 : 
    print("Valor invalido")
elif horas <= 4 :
    print(f"pagas {costo_hora * horas} en total")
else :
    print(f"Pagas {costo_hora * horas + 5000} en total")

