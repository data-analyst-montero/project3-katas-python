def filtrar_mascotas(mascotas):
    prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]

    return list(filter(lambda mascota: mascota not in prohibidas, mascotas))


mascotas = [
    "Perro",
    "Gato",
    "Mapache",
    "Loro",
    "Tigre",
    "Conejo",
    "Oso"
]

resultado = filtrar_mascotas(mascotas)
print(resultado)