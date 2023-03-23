voyelles = "aeiuotAEIUOY"

def nbVoy(chaine):
    compteur = 0
    for lettre in chaine:
        if lettre in voyelles : compteur += 1
    return compteur

print(nbVoy("sdf"))
print(nbVoy("papabidou"))