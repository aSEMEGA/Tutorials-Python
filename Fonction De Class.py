class Vehicule :
    def __init__(self,marque = "Dacia", couleur = "blanche"):
        self.marque = marque
        self.couleur = couleur

    def SeDeplacer(self):
        print(f"{self.marque} se deplace")


#Programme

maVoiture = Vehicule("Ferrarri", "Rouge")
maVoiture.SeDeplacer()