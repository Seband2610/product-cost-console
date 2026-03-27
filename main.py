# Sistema de Inventario en Consola

productos = []

# Funcion para agregar productos
def opcion_1(opcion_del_usuario):
    if opcion_del_usuario == "1":
        print("Aqui registraras el producto")
        
        nombre = input("Ingresa el nombre del producto: ")
        
        while True:
            try:
                cantidad = int(input("Ingresa la cantidad de productos: "))
                if cantidad < 0:
                    print("Error: no puede ser negativo")
                    continue
                break
            except:
                print("Error: ingresa un numero entero valido")
        
        while True:
            try:
                precio = float(input("Ingresa el precio del producto: "))
                if precio < 0:
                    print("Error: no puede ser negativo")
                    continue
                break
            except:
                print("Error: ingresa un numero valido")
        
        producto = {
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad,
        }

        productos.append(producto)
        print("Producto agregado correctamente")


# Mostrar productos
def opcion_2(opcion_del_usuario):
    if opcion_del_usuario == "2":

        if not productos:
            print("No hay productos")
            return

        for producto in productos:
            print(f"{producto['nombre']} | {producto['precio']} | {producto['cantidad']}")


# Estadisticas
def opcion_3(opcion_del_usuario):
    if opcion_del_usuario == "3":

        if not productos:
            print("No hay productos")
            return
        
        total_cantidad = 0
        total_valor = 0

        producto_mas_caro = productos[0]
        producto_mayor_stock = productos[0]

        for producto in productos:
            total_cantidad += producto["cantidad"]
            total_valor += producto["precio"] * producto["cantidad"]

            if producto["precio"] > producto_mas_caro["precio"]:
                producto_mas_caro = producto

            if producto["cantidad"] > producto_mayor_stock["cantidad"]:
                producto_mayor_stock = producto

        print(f"Total productos: {len(productos)}")
        print(f"Total unidades: {total_cantidad}")
        print(f"Valor total: {total_valor}")
        print(f"Mas caro: {producto_mas_caro['nombre']}")
        print(f"Mayor stock: {producto_mayor_stock['nombre']}")


# Eliminar
def opcion_4(opcion_del_usuario):
    if opcion_del_usuario == "4":

        if not productos:
            print("No hay productos")
            return

        nombre_buscar = input("Producto a eliminar: ")
        encontrado = False

        for producto in productos:
            if producto["nombre"] == nombre_buscar:
                productos.remove(producto)
                print("Eliminado")
                encontrado = True
                break

        if not encontrado:
            print("No existe")


# Buscar
def opcion_5(opcion_del_usuario):
    if opcion_del_usuario == "5":

        nombre_buscar = input("Producto a buscar: ")
        encontrado = False

        for producto in productos:
            if producto["nombre"] == nombre_buscar:
                print(f"{producto['nombre']} | {producto['precio']} | {producto['cantidad']}")
                encontrado = True

        if not encontrado:
            print("No encontrado")


# Actualizar
def opcion_6(opcion_del_usuario):
    if opcion_del_usuario == "6":

        nombre_buscar = input("Producto a actualizar: ")
        encontrado = False

        for producto in productos:
            if producto["nombre"] == nombre_buscar:

                # Validar nuevo precio
                while True:
                    try:
                        nuevo_precio = float(input("Nuevo precio: "))
                        if nuevo_precio < 0:
                            print("Error: no puede ser negativo")
                            continue
                        break
                    except:
                        print("Error: ingresa un numero valido")

                # Validar nueva cantidad
                while True:
                    try:
                        nueva_cantidad = int(input("Nueva cantidad: "))
                        if nueva_cantidad < 0:
                            print("Error: no puede ser negativo")
                            continue
                        break
                    except:
                        print("Error: ingresa un numero entero valido")

                producto["precio"] = nuevo_precio
                producto["cantidad"] = nueva_cantidad

                print("Actualizado")
                encontrado = True
                break

        if not encontrado:
            print("No encontrado")


# Guardar CSV
def opcion_7(opcion_del_usuario):
    if opcion_del_usuario == "7":

        if not productos:
            print("No hay productos")
            return

        ruta = input("Nombre del archivo: ")

        try:
            archivo = open(ruta, "w")

            archivo.write("nombre,precio,cantidad\n")

            for producto in productos:
                archivo.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")

            archivo.close()
            print("Guardado")

        except:
            print("Error al guardar el archivo")


# Cargar CSV
def opcion_8(opcion_del_usuario):
    if opcion_del_usuario == "8":

        ruta = input("Nombre del archivo: ")

        try:
            archivo = open(ruta, "r")

            lineas = archivo.readlines()
            archivo.close()

            productos.clear()

            for linea in lineas[1:]:
                datos = linea.strip().split(",")

                producto = {
                    "nombre": datos[0],
                    "precio": float(datos[1]),
                    "cantidad": int(datos[2])
                }

                productos.append(producto)

            print("Cargado")

        except:
            print("Error al abrir el archivo")


# MENU
while True:
    print("\nMenu")
    print("1. Agregar")
    print("2. Mostrar")
    print("3. Estadisticas")
    print("4. Eliminar")
    print("5. Buscar")
    print("6. Actualizar")
    print("7. Guardar CSV")
    print("8. Cargar CSV")
    print("0. Salir")

    menu_elegido = input("Opcion: ")

    if menu_elegido == "0":
        print("Saliendo...")
        break

    opcion_1(menu_elegido)
    opcion_2(menu_elegido)
    opcion_3(menu_elegido)
    opcion_4(menu_elegido)
    opcion_5(menu_elegido)
    opcion_6(menu_elegido)
    opcion_7(menu_elegido)
    opcion_8(menu_elegido)

        



 

    

              

              
