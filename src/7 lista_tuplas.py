def tuplas_a_strings(lista_tuplas):
    return list(map(lambda t: str(t), lista_tuplas))


tuplas = [(1, 2), (3, 4), (5, 6)]

resultado = tuplas_a_strings(tuplas)
print(resultado)