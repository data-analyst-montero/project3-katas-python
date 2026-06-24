def contar_palabras(texto):
    palabras = texto.split()
    contador = {}

    for palabra in palabras:
        if palabra in contador:
            contador[palabra] += 1
        else:
            contador[palabra] = 1

    return contador


def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    return texto.replace(palabra_original, palabra_nueva)


def eliminar_palabra(texto, palabra):
    palabras = texto.split()

    palabras_filtradas = [
        p for p in palabras if p != palabra
    ]

    return " ".join(palabras_filtradas)


def procesar_texto(texto, opcion, *args):

    if opcion == "contar":
        return contar_palabras(texto)

    elif opcion == "reemplazar":
        return reemplazar_palabras(texto, args[0], args[1])

    elif opcion == "eliminar":
        return eliminar_palabra(texto, args[0])

    else:
        return "Opción no válida"


# Caso de uso

texto = "Python es genial y Python es fácil"

# Contar palabras
resultado1 = procesar_texto(texto, "contar")
print(resultado1)


# Reemplazar palabra
resultado2 = procesar_texto(texto, "reemplazar", "Python", "Programación")
print(resultado2)


# Eliminar palabra
resultado3 = procesar_texto(texto, "eliminar", "es")
print(resultado3)