def addition(nb1 , nb2):
    return nb1 + nb2

def soustraction(nb1 , nb2):
    return nb1 - nb2

def addsous(nb1, nb2):
    return(nb1 + nb2, nb1 - nb2)

print(addsous(18,7))
(add, sous) = addsous(18,7)
print(f"addition : {add}        soustraction : {sous}")

print(addition(10,2))
print(soustraction(69,18))