


import random

nombreAdecouvrir = random.randint(1, 10)
nbr = int(input("Propose un premier nombre entre 0 et 10 : "))
nbrTrouve = False

while nbrTrouve == False:
    nbr = int(input("Propose un autre nombre entre 0 et 10 : "))
    
    if nbr < nombreAdecouvrir:
        print("C'est plus")
    elif nbr > nombreAdecouvrir:
        print("C'est moins")
        nbr = int(input("Propose un autre nombre entre 0 et 10 : "))
    else:
        print("C'est gagné")
        print("Le bon nombre est : ", nombreAdecouvrir)
        nbrTrouve = True
        break

