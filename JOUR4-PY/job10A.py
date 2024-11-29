# Demander à l'utilisateur d'entrer un nombre entier positif
nombre = int(input("Entrez un nombre entier positif : "))

# Vérifier que l'entrée est bien un entier positif
if (nombre) > 0:  # Si l'entrée est numérique et positive
   
    # Fonction pour vérifier si un nombre est pair ou impair
    def verifier_pair_impair(nombre):
        # Vérifier si le nombre est pair ou impair
        if nombre % 2 == 0:
            print(f"Le nombre {nombre} est pair.")
        else:
            print(f"Le nombre {nombre} est impair.")

    # Appeler la fonction et afficher le résultat
    verifier_pair_impair(nombre)
else:
    print("Veuillez entrer un nombre entier positif valide.")
