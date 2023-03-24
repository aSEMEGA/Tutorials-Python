'''
POO : les Classes
mot clé : class <nom de la classe>
camel case (casse de chameaux) -> chaque mot commence par une lettre capitale (Majiscule)
'''

class Vehicule:
    #Attributs (variable de classe)
    couleur = "rouge"
    marque =  "renault"

#Programme
voiture1 = Vehicule()# instance d'objet
voiture2 = Vehicule()

print(f"la voiture1 est de couleur {voiture1.couleur} et c'est une marque {voiture2.marque}")
voiture2.couleur = "noir"
voiture2.marque = "toyota"
print(f"la voiture1 est de couleur {voiture2.couleur} et c'est une marque {voiture2.marque}")