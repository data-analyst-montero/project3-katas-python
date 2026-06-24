def calcular_resultado(notas, nota_aprobado=5):
    media = sum(notas) / len(notas)

    if media >= nota_aprobado:
        estado = "aprobado"
    else:
        estado = "suspenso"

    return (media, estado)


notas = [6, 7, 5, 8, 4]

resultado = calcular_resultado(notas)
print(resultado)