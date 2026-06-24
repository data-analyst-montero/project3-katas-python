def palabras_mas_largas(texto, n):
    palabras = texto.split()
    return list(filter(lambda palabra: len(palabra) > n, palabras))


frase = "Python es un lenguaje de programación muy potente y no tan dificil de aprender"

resultado = palabras_mas_largas(frase, 5)
print(resultado)