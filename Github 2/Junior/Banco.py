"""11. Banco “PythonBank” – Simulación de ahorro mensual
Como cliente, quiero usar un for que sume mi ahorro mensual durante 6 meses.
Si en algún mes el total supera $1,000,000, mostrar “¡Meta alcanzada!”.
Al final, mostrar el total acumulado."""

total_ahorro = 0 
for mes in range(1, 7): 
    ahorro = float(input(f"Ingrese el monto ahorrado en el mes {mes}: $"))
    total_ahorro += ahorro 

    if total_ahorro > 1_000_000:
        print("¡Meta alcanzada!")
        break 

print(f"Total acumulado: ${total_ahorro:}")
