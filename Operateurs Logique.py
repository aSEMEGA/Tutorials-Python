'''
Operateurs Logique

not    n'est pas
and    et logique
or     ou logique
'''

username = "jean"
password = "1234"

print("Interface de connexion de la naza")
print("---------------------------------")

userinput = input("Login : ")
passinput = input("password :")

if userinput == username or passinput == password :
    print(f"login ou password invalid")

elif userinput == username and passinput == password:
     print(f"Bienvenue {userinput} a la naza")
else:
    print("Authentification non valide")

homme = False

if not homme:
    print(f"Bonjour Madame")

