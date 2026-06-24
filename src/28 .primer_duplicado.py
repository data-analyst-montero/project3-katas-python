def primer_duplicado(lista):
    vistos = set()

    for elemento in lista:
        if elemento in vistos:
            return elemento
        vistos.add(elemento)

    return None


numeros = [4, 2, 7, 3, 2, 8, 4]

resultado = primer_duplicado(numeros)

print(resultado)