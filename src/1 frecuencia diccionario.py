def frecuencia_letras(texto):
    frecuencias = {}

    for caracter in texto:
        if caracter != " ":  # No cuenta espacios
            frecuencias[caracter] = frecuencias.get(caracter, 0) + 1

    return frecuencias


cadena = "The Power"
resultado = frecuencia_letras(cadena)
print(resultado)