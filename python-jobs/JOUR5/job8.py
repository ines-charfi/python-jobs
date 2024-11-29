# Créer la liste L
Liste = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]
print("Ma liste est :", Liste)

# Initialiser une variable pour la somme des nombres pairs
nbres_paires = 0

# Parcourir chaque élément de la liste
for nombre in Liste:
    # Vérifier si le nombre est pair
    if nombre % 2 == 0:
        nbres_paires += nombre  # Ajouter le nombre pair à la somme

# Afficher la somme des nombres pairs
print("La somme des valeurs paires dans la liste est :", nbres_paires)
