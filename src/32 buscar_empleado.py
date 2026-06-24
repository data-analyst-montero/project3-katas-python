def buscar_empleado(nombre_completo, empleados):
    for empleado in empleados:
        if empleado["nombre"] == nombre_completo:
            return f"{nombre_completo} trabaja como {empleado['puesto']}"

    return "La persona no trabaja aquí."


# Ejemplo de uso
empleados = [
    {"nombre": "Ana García López", "puesto": "Programadora"},
    {"nombre": "Luis Pérez Martín", "puesto": "Diseñador"},
    {"nombre": "Marta Sánchez Ruiz", "puesto": "Analista"}
]

resultado = buscar_empleado("Luis Pérez Martín", empleados)

print(resultado)