sumar_listas = lambda lista1, lista2: list(map(lambda x, y: x + y, lista1, lista2))


lista1 = [1, 2, 3, 4]
lista2 = [10, 20, 30, 40]

resultado = sumar_listas(lista1, lista2)

print(resultado)