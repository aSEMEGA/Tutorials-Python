'''
les fonctions
mot clé def(define)
'''
def table():
    for i in range(11):
        print(f"{i} * 2 = {2 * i}")

def table1(x):
    for i in range(11):
        print(f"{i} * {x} = {2 * i}")

def direBonjour(nom = "sy", prenom = "ali", age = 10):
    print(f"bonjour je m'appelle {prenom} {nom} et j'ai {age} ans")

table()
print("---------")
table1(4)
print("---------")
direBonjour()
