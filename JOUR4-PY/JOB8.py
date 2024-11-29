#demander à l'utilisateur de saisir les données
type = input("saisir un type :  ")
saison = input("saisir une saison :  ")
#definition de la fonction caddie
def caddie(type , saison):
    if type =="fruits" and saison == "hiver":
        print("« orange, mandarine et kiwi »")
    elif type == "fruits" and saison == "été":
        print("« Poire, fraise, cassis »")
    elif type == "légume" and saison == "hiver":
        print("« carotte, topinambour, endive »")
    elif type == "légume" and saison =="été":
        print("« artichaut, aubergine,navet »")
    else:
        print("saisir un autre type et une autre saison")
#appeler la fonction caddie
caddie(type,saison)
        
        
