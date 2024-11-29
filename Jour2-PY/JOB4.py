# Demander à l'utilisateur de saisir un entier N
N = int(input("Entrez un entier N (supérieur à 0) : "))

    # Parcourir les nombres de 1 à N
for i in range(1, N + 1):
        print(f"Table de multiplication de {i}:")
        # Afficher les multiples de i (de 1 à 10)
        for j in range(1, 11):
            print(f"{i} x {j} = {i * j}")
        print()  # Pour ajouter une ligne vide entre les tables



