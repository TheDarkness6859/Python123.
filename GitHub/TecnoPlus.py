print("Coloca tus notas desde 0.0 hasta 5.0")
nota1 = float(input("Nota Técnica :"))
nota2 = float(input("Nota Lógica:"))
Prueba_tecnica = nota1 
Prueba_Logica = nota2 
total_nota = Prueba_tecnica * 0.7 + Prueba_Logica * 0.3

if total_nota < 2 :
    print("Reprobado")
elif total_nota <= 2 < 3 :
    print("Revisión")
elif total_nota > 5.0 :
    print("Ingrese una nota correcta de 0.0 hasta 5.0")
else : 
    print("Aprobado")