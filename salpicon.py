frutas=[]
print("****************BIENVENIDO AL SALPICON*******************")

for i in range(5):
    nombre=input("ingresa el nombre de la fruta: ")

    precio=int(input("ingresa el precio de la fruta: "))
    
    fruta={
        "nombre": nombre,
        "precio":precio
    }
    frutas.append(fruta)

def obtener_precio(fruta):
    return fruta["precio"]

frutasOrdenada=sorted(frutas,key=obtener_precio,reverse=True)

for fruta in frutasOrdenada:
    print(fruta)
