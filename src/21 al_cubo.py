def al_cubo(lista):
    return list(map(lambda x: x*x*x, lista))

lista = [1,0,2,4,6 ]

resultado = al_cubo(lista)

print(resultado)