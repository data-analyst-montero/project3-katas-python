def diferencia_listas(lista1, lista2):
    return list(map(lambda x, y: x - y, lista1, lista2))


lista1 = [10, 20, 30, 40]
lista2 = [1, 2, 3, 4]

resultado = diferencia_listas(lista1, lista2)
print(resultado)