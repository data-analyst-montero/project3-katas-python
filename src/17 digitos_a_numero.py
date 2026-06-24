from functools import reduce

def digitos_a_numero(lista_digitos):
    if not lista_digitos:
        return 0

    if not all(0 <= digito <= 9 for digito in lista_digitos):
        raise ValueError("Todos los elementos deben ser dígitos entre 0 y 9.")

    return reduce(lambda acumulador, digito: acumulador * 10 + digito, lista_digitos)


print(digitos_a_numero([1, 2, 3, 4]))  
print(digitos_a_numero([0, 5, 8]))    