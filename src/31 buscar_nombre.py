class NombreNoEncontradoError(Exception):
    pass


def buscar_nombre():
    try:
        nombres = input("Introduce una lista de nombres separados por comas: ")
        lista_nombres = nombres.split(",")

        nombre_buscar = input("Introduce el nombre que quieres buscar: ")

        # Limpiar espacios
        lista_nombres = [nombre.strip() for nombre in lista_nombres]

        if nombre_buscar in lista_nombres:
            print(f"El nombre {nombre_buscar} fue encontrado.")
        else:
            raise NombreNoEncontradoError(
                f"El nombre {nombre_buscar} no está en la lista."
            )

    except NombreNoEncontradoError as e:
        print(f"Error: {e}")


buscar_nombre()