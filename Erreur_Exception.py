'''
Erreur et Exception
---------------------
try :       tester un bloc de code
except :    le bloc est executer en d'erreur
'''

nb1 = input("nb1")
nb2 = input("nb2")
try:
    print(int(nb1 / nb2))

except :
    print("attention li y'a une erreur")