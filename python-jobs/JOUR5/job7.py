# Créer la liste L
Liste = [8, 24, 48, 2, 16]
print("Ma liste est :" , Liste)

# Initialiser un compteur pour les multiples de 3
nbre_multiple = 0

# Parcourir chaque élément de la liste
for nombre in Liste:
    # Vérifier si le nombre est un multiple de 3
    if nombre % 3 == 0:
        nbre_multiple += 1  # Incrémenter le compteur si le nombre est un multiple de 3

# Afficher le nombre de multiples de 3
print("Il y a", nbre_multiple, "multiples de 3 dans la liste.")
