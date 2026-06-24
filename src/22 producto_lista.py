from functools import reduce

def producto_lista(numeros):
    return reduce(lambda x, y: x * y, numeros)

lista = [2, 3, 4, 5]

resultado = producto_lista(lista)

print(resultado)