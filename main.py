import random

helados = []  # Lista para almacenar los helados


# Menu de opciones
print("Gestión de Helados")
print("1. Agregar un helado")
print("2. Ver lista de helados")
print("3. Modificar un helado")
print("4. Eliminar un helado")
print("5. Salir")

opcion = 100

while opcion != 5:

    try:
        opcion = int(input("Digita una opcion del menu"))

        if opcion == 1:  # Agregar un helado
            helado = {
                "id": random.randint(1, 100),
                "nombre": input("Digita el nombre del helado: "),
                "presentacion": input("Digita la presentación del helado: "),
                "cantidad": int(input("Digita la cantidad: ")),
                "precio": int(input("Digita el precio del helado: "))
            }
            helados.append(helado)
            print("helado agragado correctamente")

        elif opcion == 2:  # Ver lista de helados
            if not helados:
                print("No hay helados en tu lista")
            else:
                print("Lista de helados:")
                for heladoIterado in helados:
                    print(
                        f"ID: {heladoIterado['id']}, Nombre: {heladoIterado['nombre']},Presentacion: {heladoIterado['presentacion']}, Precio: {heladoIterado['precio']}, Cantidad: {heladoIterado['cantidad']}")

        elif opcion == 3:  # Modificar un helado
            idHeladoABuscar = int(
                input("Cual es el id del helado que deseas modificar?"))
            encontrado = False
            for heladoBuscado in helados:
                if idHeladoABuscar == heladoBuscado["id"]:
                    print("Helado encontrado. Ingresa los nuevos valores:")
                    heladoBuscado["nombre"] = input("Nuevo nombre: ")
                    heladoBuscado["presentacion"] = input(
                        "Nueva presentación: ")
                    heladoBuscado["cantidad"] = int(
                        input("Nueva cantidad: "))
                    heladoBuscado["precio"] = int(input("Nuevo precio: "))
                    encontrado = True
                    print("helado modificado con éxito!")
                    break

                if not encontrado:
                    print("Helado no encontrado.")

        elif opcion == 4:  # Eliminar un helado
            idHeladoAEliminar = int(
                input("¿Cuál es el ID del helado a eliminar? "))
            helados = [E for E in helados if E["id"]
                       != idHeladoAEliminar]
            print("Helado eliminado con éxito!")

        elif opcion == "5":  # Salir
            print("Saliendo del programa")

        else:
            print("Opción inválida, intente nuevamente.")

    except ValueError:
        print("Ingresa un numero valido")
