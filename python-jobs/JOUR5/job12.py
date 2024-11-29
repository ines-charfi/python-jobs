#Créer une liste
Liste = [7, 11, 42, 39, 2]
print("Ma liste avant le tri est :", Liste)
# Fonction pour trier la liste dans l'ordre croissant
def trie_liste(Liste):
    # Comparer chaque élément avec les autres pour le placer au bon endroit
    for i in range(len(Liste)):  # On parcourt tous les éléments de la liste
        for j in range(i + 1, len(Liste)):  # On compare l'élément courant avec les suivants
            if Liste[i] > Liste[j]:  # Si l'élément courant est plus grand que l'autre
                # Échanger les éléments
                Liste[i], Liste[j] = Liste[j], Liste[i]
    return Liste



# Appeler la fonction pour trier la liste
Liste_triee = trie_liste(Liste)

# Afficher la liste triée
print("Liste triée dans l'ordre croissant :", Liste_triee)
