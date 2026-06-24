def enmascarar(valor):
    texto = str(valor)

    if len(texto) <= 4:
        return texto

    return "#" * (len(texto) - 4) + texto[-4:]


dato = "123456789"

resultado = enmascarar(dato)

print(resultado)