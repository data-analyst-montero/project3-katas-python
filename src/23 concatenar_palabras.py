from functools import reduce

def concatenar_palabras(lista):
    return reduce(lambda x, y: x + y, lista)


palabras = ["Python", " es ", "el", " mejor!"]

resultado = concatenar_palabras(palabras)

print(resultado)