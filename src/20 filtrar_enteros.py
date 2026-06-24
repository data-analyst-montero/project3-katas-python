def filtrar_enteros(lista):
    return list(filter(lambda x: isinstance(x, int), lista))

lista = [10, "hola", 25, "Python", 7, 3.5, "50"]

resultado = filtrar_enteros(lista)

print(resultado)