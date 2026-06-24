import math

def calcular_area(figura, datos):

    if figura == "rectangulo":
        base, altura = datos
        return base * altura

    elif figura == "circulo":
        radio = datos[0]
        return math.pi * radio ** 2

    elif figura == "triangulo":
        base, altura = datos
        return (base * altura) / 2

    else:
        return "Figura no válida"


# Ejemplos de uso

print(calcular_area("rectangulo", (5, 3)))
print(calcular_area("circulo", (3,)))
print(calcular_area("triangulo", (6, 2)))