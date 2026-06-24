def estudiantes_aprobados(estudiantes):
    return list(filter(lambda estudiante: estudiante["calificacion"] >= 90, estudiantes))


# Lista de estudiantes
estudiantes = [
    {"Estudiante": "Ana", "edad": 20, "calificacion": 95},
    {"Estudiante": "Luis", "edad": 22, "calificacion": 85},
    {"Estudiante": "Marta", "edad": 19, "calificacion": 90},
    {"Estudiante": "Carlos", "edad": 21, "calificacion": 78},
    {"Estudiante": "Sofía", "edad": 20, "calificacion": 98}
]


# Filtrar estudiantes con calificación >= 90
resultado = estudiantes_aprobados(estudiantes)

print(resultado)