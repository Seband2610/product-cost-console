print("Inventario de productos")

productos = []


print("menu")

print("1. Agregar productos")
print("2. Ver productos")
print("3. Actualizar productos")
print("4. Eliminar productos")
print("0. Salir")

opcion=input("Ingrese una opcion: ")
if opcion == "1":
    print("Aqui ingresaras el nombre del producto")

    nombre= input("Ingresa el nombre del producto: ")
    cantidad= int(input("Ingresa la cantidad de productos: "))
    precio= float( input("Ingresa el precio del producto: "))

    producto = {

    "nombre": nombre,
    "precio": precio,
    "cantidad": cantidad,
    }
    productos.append(producto)
    print("Producto agregado correctamente")

if opcion == "2":
    print("A continuacion veras la lista de productos")
    for producto in productos:
        print(producto["nombre"])



 

    

              

              
