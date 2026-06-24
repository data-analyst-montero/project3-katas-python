def buscar_palabras(lista_palabras, palabra_objetivo):
    resultado = []

    for palabra in lista_palabras:
        if palabra_objetivo in palabra:
            resultado.append(palabra)

    return resultado


palabras = ["ratón", "libreta", "móvil", "perro", "libreria", "gato", "libro"]
objetivo = "libr"

print(buscar_palabras(palabras, objetivo))