def letras_mayus_minus(caracteres):
    caracteres_unicos = set(caracteres)
    return list(map(lambda letra: (letra.upper(), letra.lower()), caracteres_unicos))


letras = {'a', 'b', 'c', 'a', 'B'}

resultado = letras_mayus_minus(letras)
print(resultado)