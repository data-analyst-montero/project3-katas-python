class ListaVaciaError(Exception):
    """Excepción lanzada cuando la lista está vacía."""
    pass


def calcular_promedio(numeros):
    if not numeros:
        raise ListaVaciaError("No se puede calcular el promedio de una lista vacía.")

    return sum(numeros) / len(numeros)


try:
    lista = [10, 20, 30, 40]
    promedio = calcular_promedio(lista)
    print(f"El promedio es: {promedio}")

except ListaVaciaError as e:
    print(f"Error: {e}")