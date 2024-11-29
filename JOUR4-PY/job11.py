# Demander à l'utilisateur d'entrer un nombre de minutes
minutes = int(input("Entrez un nombre de minutes : "))

# Définir la fonction time_to_text
def time_to_text(minutes):
    # Calculer le nombre d'heures
    heures = minutes // 60  # Diviser les minutes par 60 pour obtenir les heures

    # Calculer les minutes restantes
    calcul_minutes = minutes % 60  # Le reste de la division par 60 donne les minutes restantes

    # Afficher le résultat
    print(heures, "heures et", calcul_minutes, "minutes")



# Appeler la fonction pour afficher le résultat
time_to_text(minutes)
