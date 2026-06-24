def son_anagramas(palabra1, palabra2):
    return sorted(palabra1.lower()) == sorted(palabra2.lower())


# Ejemplo de uso
palabra1 = "Roma"
palabra2 = "Amor"

resultado = son_anagramas(palabra1, palabra2)

print(resultado)