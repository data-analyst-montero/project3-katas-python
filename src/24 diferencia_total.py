from functools import reduce

def diferencia_total(lista):
    return reduce(lambda x, y: x - y, lista)


numeros = [20, 5, 3, 2]

resultado = diferencia_total(numeros)

print(resultado)