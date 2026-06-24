def clasificar_nota(nota):
    if 0 <= nota <= 69:
        return "Insuficiente"
    elif 70 <= nota <= 79:
        return "Bien"
    elif 80 <= nota <= 89:
        return "Muy bien"
    elif 90 <= nota <= 100:
        return "Excelente"
    else:
        return "Nota no válida"


# Pedir nota al usuario
nota_usuario = int(input("Introduce la calificación del alumno (0-100): "))

resultado = clasificar_nota(nota_usuario)

print(f"La calificación es: {resultado}")