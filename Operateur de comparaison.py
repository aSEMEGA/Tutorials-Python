'''
Operateur de comparaison

  ==      égal
  !=      différent de (non égal)
  >       Strictement supérieur
  >=      supérieur ou égal
  <       Strictement inferieur
  <=      inférieur ou égal
  '''

nb1 = 10
nb2 = 10

if nb1 == nb2:
    print(f"{nb1} est égal à {nb2}")
  
a = 2
b = 5
if a > b:
    print(f"{a} est superieur à {b}")
else:
        print(f"{a} est inferieur à {b}")
if a < b:
    print(f"{a} est inferieur à {b}")
else:
     print(f"{a} est superieur à {b}")

if a >= b:
    print(f"{a} est superieur ou égal à {b}")
else:
    print(f"{a} est inferieur ou égal à {b}")
if a <= b:
    print(f"{a} est inferieur ou égal à {b}")
else:
    print(f"{a} est superieur ou égal à {b}")
if a!= b:
    print(f"{a} est different à {b}")
