#Le preguntamos al usuario su edad

print("Diligencia tu edad y documento")
Edad = int(input("Edad :"))

if Edad < 18 : #Buscamos identificar la edad para generar una acción pertinente
    print("Entrada denegada")
else: #Si no se cumple el if se crean indicaciones para los mayores de edad
    print("Puedes entrar solo si tienes documento")
    documento = str(input("Tienes documento?")) #Se pide el documento
    if documento == "si" : #se detecta la respuesta
        input("pon tu documento")
        print("Puede pasar")
    elif documento != "no" : #este elif permite eliminar respuestas innecesarias
        print("Que dices? lmao, pon algo coherente")
    else : # por ultimo si no tiene documento se le indica al usuario
        print("Debe presentar el documento")