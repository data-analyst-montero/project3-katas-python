def doble (x):
    return x * 2

numeros = [1, 2, 3, 4, 5]
dobles = list(map(doble , numeros))

print(dobles)