# Sistema de Inventario en Consola
# Este programa deja agregar productos, verlos y calcular datos basicos

# Lista donde se guardan los productos
productos = []

# Funcion para agregar productos
def opcion(opcion_del_usuario):
    if opcion_del_usuario == "1":
        print("Aqui registraras el producto")
        
        # Pedir datos al usuario
        nombre = input("Ingresa el nombre del producto: ")
        
        # Validar cantidad
        while True:
            try:
                cantidad = int(input("Ingresa la cantidad de productos: "))
                break
            except:
                print("Error: ingresa un numero entero valido")
        
        # Validar precio
        while True:
            try:
                precio = float(input("Ingresa el precio del producto: "))
                break
            except:
                print("Error: ingresa un numero valido")
        
        # Calcular costo total
        costo_total = precio * cantidad
        
        # Mostrar datos ingresados
        print(f"Producto: {nombre}")
        print(f"Cantidad: {cantidad}")
        print(f"Precio: {precio}")
        print(f"Costo total: {costo_total}")

        # Guardar producto en un diccionario
        producto = {
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad,
        }

        # Agregar el producto a la lista
        productos.append(producto)
        print("Producto agregado correctamente")


# Funcion para mostrar todos los productos
def opcion_2(opcion_del_usuario):
    if opcion_del_usuario == "2":
        print("A continuacion veras la lista de productos:")

        # Verificar si no hay productos
        if not productos:
            print("No hay productos en el inventario")
            return

        # Recorrer la lista y mostrar cada producto
        for producto in productos:
            print(f"Producto: {producto['nombre']} | Precio: {producto['precio']} | Cantidad: {producto['cantidad']}")


# Funcion para calcular estadisticas
def opcion_3(opcion_del_usuario):
    if opcion_del_usuario == "3":

        # Verificar si la lista esta vacia
        if not productos:
            print("No hay productos en el inventario")
            return
        
        total_cantidad = 0
        total_valor = 0

        # Recorrer productos para hacer los calculos
        for producto in productos:
            total_cantidad += producto["cantidad"]
            total_valor += producto["precio"] * producto["cantidad"]

        # Mostrar resultados
        print(f"Total de productos: {len(productos)}")
        print(f"Suma total de cantidades: {total_cantidad}")
        print(f"Valor total del inventario: {total_valor}")
        

# Funcion para eliminar un producto
def opcion_4(opcion_del_usuario):
    if opcion_del_usuario == "4":

        # Verifica si hay productos
        if not productos:
            print("No hay productos")
            return

        nombre_buscar = input("Ingresa el nombre del producto a eliminar: ")
        encontrado = False

        # Recorre la lista
        for producto in productos:
            if producto["nombre"] == nombre_buscar:
                productos.remove(producto)
                print("Producto eliminado")
                encontrado = True
                break

        # Si no lo encontró
        if not encontrado:
            print("El producto no existe")


# Inicio del programa
print("Inventario de productos")

# Menu principal
while True:
    print("\nMenu")
    print("1. Agregar productos")
    print("2. Ver productos")
    print("3. Ver estadisticas")
    print("4. Eliminar productos")
    print("0. Salir")

    # Pedir opcion al usuario
    menu_elegido = input("Ingrese una opcion: ")

    # Salir del programa
    if menu_elegido == "0":
        print("Saliendo del programa...")
        break

    # Llamar funciones segun opcion
    opcion(menu_elegido)
    opcion_2(menu_elegido)
    opcion_3(menu_elegido)
    opcion_4(menu_elegido)


# Fin del programa

        



 

    

              

              
