'''
Structure de données : dictionnaires

dico = {}  dictionnaire vide
dico  = {<key> : <value>}        paire(clé:valeur)

'''

dico = {"prenom": "abba", "nom" : "bocoum", "age": 44}
for value in dico.values() :
    print(value)
print("--------------")
for key in dico.keys() :
    print(key)
print("--------------")
for key, value in dico.items() :
    print(key,value)