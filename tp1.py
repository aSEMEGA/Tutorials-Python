print("Que voudriez-vous calculer")
print("1.la Surface\n2.le Volume")

choix = (int(input("Entrer 1 ou 2\n > ")))
print("--------------")
largeur = (int(input("Entrer la largeur :>")))
longueur = (int(input("Entrer la longueur :>")))
if choix == 1:
    Surface = longueur * largeur
    print("la Surface est : ", Surface)

elif choix == 2:
    hauteur = (float(input("Entrer la hauteur :>")))
    Volume = longueur * largeur * hauteur
    print("le volume est : ", Volume)
