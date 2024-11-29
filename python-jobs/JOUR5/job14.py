def my_long_word(n, chaine):
    resultat = ""
    for word in chaine.split():
        compteur = 0
        for caractère in word:
            compteur += 1
        if compteur > n:
            resultat += word + " "
    return resultat[:-1]  # On enlève le dernier espace

# Exemple d'utilisation
texte = "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance"
print(my_long_word(3, texte))
