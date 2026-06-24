def longitud_palabras(frase):
    palabras = frase.split()
    return list(map(len, palabras))


frase = "Python es mágico"
resultado = longitud_palabras(frase)

print(resultado)