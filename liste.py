'''
Structrure de donnée : les listes
--------------------------------
append          ajouter un element à la fin de la liste
insert          ajouter un element selon un index
remove          supprimer un element par sa valeur
pop             supprimer un element par son index
index           afficher l'index selon une valeur
count           nombre de fois ou l'element apparait
sort            trier par ordere croissant
reverse         inverser l'ordre de la liste
copy            copie d'une liste
extend          etendre une liste
'''

maliste = ["ali","bouba","oumar","bah"]
maliste2 = [1,2,12,15]

maliste.append("ada")
for element in maliste:
    print(element)
print("----------")

maliste.insert(1,"lana")
for element in maliste:
    print(element)
print("-------")

maliste.remove(1,"bouba")
for element in maliste:
    print(element)
print("-------")

for element in maliste:
    print(element)

maliste2.extend(maliste)
print("---------")

for element in maliste2:
    print(element)