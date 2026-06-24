def clasificar_hora(hora):
    if hora >= 0 and hora < 12:
        return "Es de día"
    elif hora >= 12 and hora < 20:
        return "Es tarde"
    elif hora >= 20 and hora <= 23:
        return "Es de noche"
    else:
        return "Hora no válida"


# Pedir hora al usuario
hora_usuario = int(input("Introduce la hora (0-23): "))

resultado = clasificar_hora(hora_usuario)

print(resultado)