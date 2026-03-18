
def opcion(opcion_del_usuario):
    if opcion_del_usuario == "1":
        print("Aqui registraras el producto")
        nombre= input("Ingresa el nombre del producto: ")
        cantidad= int(input("Ingresa la cantidad de productos: "))
        precio= float( input("Ingresa el precio del producto: "))
        costo_total= precio * cantidad
        print("producto: ", nombre)
        print("cantidad: ", cantidad)
        print("precio: ", precio)
        print("costo_total: ", costo_total)

        producto = {

        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad,
        }
        productos.append(producto)
        print("Producto agregado correctamente")


#inicio del programa
print("Inventario de productos")

productos = []

#muestra el menu del programa
print("menu")

print("1. Agregar productos")
print("2. Ver productos")
print("3. Actualizar productos")
print("4. Eliminar productos")
print("0. Salir")
#Llama a la funcion
menu_elegido=input("Ingrese una opcion: ")
opcion(menu_elegido)


if opcion == "2":
    print("A continuacion veras la lista de productos")
    for producto in productos:
        print(producto["nombre"])



 

    

              

              
