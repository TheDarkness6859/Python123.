"""23. Banco “LoopBank” – Simulación de intereses
Como analista financiero, quiero una función calcularInteres() que reciba un monto y una tasa (porcentaje) y retorne el valor final después de aplicar el interés una vez.
El programa principal debe pedir los datos y mostrar el resultado."""

def calcularInteres(monto, tasa):
    interes = monto * (tasa / 100)
    valor_final = monto + interes
    return valor_final

monto = float(input("Ingrese el monto inicial: "))
tasa = float(input("Ingrese la tasa de interés (%): "))

resultado = calcularInteres(monto, tasa)
print("El valor final con interés es:", resultado)
