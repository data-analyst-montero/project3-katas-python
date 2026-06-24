class Arbol:
    def __init__(self):
        # Inicializa el árbol con tronco de longitud 1 y sin ramas
        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self):
        # Aumenta la longitud del tronco en 1
        self.tronco += 1

    def nueva_rama(self):
        # Añade una nueva rama con longitud inicial 1
        self.ramas.append(1)

    def crecer_ramas(self):
        # Aumenta en 1 la longitud de todas las ramas
        self.ramas = [rama + 1 for rama in self.ramas]

    def quitar_rama(self, posicion):
        # Elimina una rama según su posición
        if 0 <= posicion < len(self.ramas):
            self.ramas.pop(posicion)
        else:
            print("La posición de la rama no existe.")

    def info_arbol(self):
        # Muestra la información del árbol
        print(f"Longitud del tronco: {self.tronco}")
        print(f"Número de ramas: {len(self.ramas)}")
        print(f"Longitudes de las ramas: {self.ramas}")

arbol = Arbol()

arbol.crecer_tronco()
arbol.nueva_rama()
arbol.nueva_rama()
arbol.crecer_ramas()

arbol.info_arbol()

arbol.quitar_rama(0)

arbol.info_arbol()