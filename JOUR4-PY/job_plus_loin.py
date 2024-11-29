# Demander à l'utilisateur d'entrer une chaîne
chaine = input("Entrez une chaîne de caractères : ")

# Définir la fonction pour inverser une chaîne de caractères
def inverser_chaine(chaine):
    chaine_inversée = ""  # Créer une chaîne vide pour stocker le résultat
    # Boucle pour parcourir la chaîne de la fin vers le début
    for i in range(len(chaine) - 1, -1, -1):  
        chaine_inversée += chaine[i]  # Ajouter le caractère à la chaîne inversée
    return chaine_inversée



# Appeler la fonction et afficher la chaîne inversée
print("Chaîne inversée :", inverser_chaine(chaine))
