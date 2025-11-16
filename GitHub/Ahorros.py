producto = 2000
descuento1 = 0.15
descuento2 = 0.05
envio = 5000


print("bienvenidos ahorromax")
cantidad=int(input("que cantidad deseas "))
if cantidad < 0:
    print("no es valido")
if cantidad <=10: 
    total= (cantidad * producto)- envio 
    print (total)
if cantidad >10:
    total= (cantidad* producto)
    total1= total-(total*descuento2)
    print(total1+envio)
if cantidad >=30:
    total= (cantidad* producto)
    total1= total-(total*descuento1)
    print(total1)