# Créer une liste quelconque non vide
L = [15, 13, 328, 33, 55]

# Afficher la liste avant l'échange
print("La liste avant l'échange est : ", L)

# Échanger la première et la dernière valeur de la liste
premier = L[0]  # Sauvegarder la première valeur
dernier = L[-1]  # Sauvegarder la dernière valeur

L[0] = dernier  # Remplacer la première valeur par la dernière
L[-1] = premier  # Remplacer la dernière valeur par la première

# Afficher la liste après l'échange
print("La liste après l'echange est : ", L)
