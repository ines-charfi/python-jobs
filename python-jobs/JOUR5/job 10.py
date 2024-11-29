# Créer la liste L
Liste = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

# Initialiser le produit à 1
produit = 1

# Parcourir chaque élément de la liste
for nombre in Liste:
    # Vérifier si le nombre est dans l'intervalle [25, 90]
    if 25 <= nombre <= 90:
        produit = produit * nombre  # Multiplier le produit par le nombre

# Afficher le résultat
print("Le produit des valeurs dans l'intervalle [25, 90] est :", produit)
