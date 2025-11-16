chocolate = 4000
vainilla = 3500
topping = 1000

sabor = input("Ingresa el sabor del helado (chocolate o vainilla): ").lower()

if sabor == "chocolate" or sabor == "vainilla":

    desea_topping = input("¿Quieres topping? (si / no): ").lower()
    
    precio = chocolate if sabor == "chocolate" else vainilla

    if desea_topping == "si":
        precio += topping
    
    print(f"El total a pagar por tu helado de {sabor} es: ${precio}")
else:
    print("Sabor no disponible")
