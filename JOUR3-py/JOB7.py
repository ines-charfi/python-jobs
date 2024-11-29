# Créer la chaîne répétée 10 fois
chaine = "abcdefghijklmnopqrstuvwxyz" * 10

# Initialiser une variable pour suivre le nombre de caractères à afficher
i = 1

# Boucle pour afficher la pyramide
while i <= 30:  # On veut afficher 26 lignes, chaque ligne avec un caractère de plus
    print(chaine[:i])  # Affiche les 'i' premiers caractères de la chaîne
    i += 1  # Augmente le nombre de caractères à afficher pour la prochaine ligne
