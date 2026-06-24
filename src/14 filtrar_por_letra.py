def filtrar_por_letra(lista_palabras, letra):
    return list(filter(lambda palabra: palabra.startswith(letra), lista_palabras))


palabras = ["casa", "piso", "cerro", "coche", "hoja", "huracan"]

resultado = filtrar_por_letra(palabras, "h")
print(resultado)