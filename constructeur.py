class Vehicule:
    def __init__(self, marque, couleur):
        self.marque = marque
        self.couleur = couleur


#Programme
voiture1 = Vehicule("Toyota", "Blanc")
voiture2 = Vehicule("Avensis", "Gris")

print(f"la voiture1 est de couleur {voiture1.couleur} et c'est une marque {voiture1.marque}")

print(f"la voiture2 est de couleur {voiture2.couleur} et c'est une marque {voiture2.marque}")