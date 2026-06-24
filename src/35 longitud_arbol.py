class Arbol:
    def __init__(self):
        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self):
        self.tronco += 1

    def nueva_rama(self):
        self.ramas.append(1)

    def crecer_ramas(self):
        self.ramas = [rama + 1 for rama in self.ramas]

    def quitar_rama(self, posicion):
        if 0 <= posicion < len(self.ramas):
            self.ramas.pop(posicion)
        else:
            print("No existe esa posición de rama.")

    def info_arbol(self):
        return {
            "Longitud del tronco": self.tronco,
            "Número de ramas": len(self.ramas),
            "Longitudes de las ramas": self.ramas
        }


# 1. Crear un árbol
arbol = Arbol()

# 2. Hacer crecer el tronco una unidad
arbol.crecer_tronco()

# 3. Añadir una nueva rama
arbol.nueva_rama()

# 4. Hacer crecer todas las ramas una unidad
arbol.crecer_ramas()

# 5. Añadir dos nuevas ramas
arbol.nueva_rama()
arbol.nueva_rama()

# 6. Retirar la rama situada en la posición 2
arbol.quitar_rama(2)

# 7. Obtener información del árbol
informacion = arbol.info_arbol()

print(informacion)