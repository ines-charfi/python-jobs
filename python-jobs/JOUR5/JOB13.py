# Liste initiale avec des doublons
Liste = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
print("Ma liste avant la modification est : ", Liste)

# Créer une nouvelle liste vide pour stocker les éléments uniques
Liste_sans_doublons = []

# Parcourir chaque élément de la liste L
for element in Liste:
    # Si l'élément n'est pas déjà dans la nouvelle liste, on l'ajoute
    if element not in Liste_sans_doublons:
        Liste_sans_doublons.append(element)

# Afficher la liste sans doublons
print("Liste sans doublons :", Liste_sans_doublons)
