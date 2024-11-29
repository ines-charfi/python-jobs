# Créer une liste "L" d'au moins 5 entiers
Liste = [12, 18, 26, 46, 33]

# Afficher la deuxième valeur de la liste (index 1)
print("La deuxième valeur de la liste est :", Liste[1])

# Fonction pour remplacer L[3] par la somme des cases voisines L[2] et L[4]
def remplacer_somme_case():
    Liste[3] = Liste[2] + Liste[4]  # Remplacer L[3] par la somme de L[2] et L[4]
    print("Liste après modification :", Liste)  # Afficher la liste après modification

# Appeler la fonction pour modifier la liste
remplacer_somme_case()

# Afficher la dernière valeur de la liste (index 4)
print("La dernière valeur de la liste est :", Liste[-1])
