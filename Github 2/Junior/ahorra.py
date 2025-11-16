"""14. Tienda “Ahorra Más” – Caja registradora básica
Como cajero, quiero pedir montos de venta hasta que el usuario escriba 0.
Si la venta supera $100,000, mostrar “Venta destacada”.
Al final, mostrar el total vendido."""

print("Ahorro mas")

precio=float(input("precio de ventas:"))

while True:
    ventas=int(input("numeros de ventas:"))
    resultado=ventas*precio
    if resultado >=100000:
     print(f"total de la venta {resultado} , venta destacada") 
    elif ventas == 0:
        break
    else :
       print(resultado)