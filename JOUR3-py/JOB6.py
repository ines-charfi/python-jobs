# Demander à l'utilisateur d'entrer un nombre
nombre = int(input("Entrez un nombre : "))

# Vérifier si le nombre est pair
if nombre % 2 == 0:
    print(f"Le nombre {nombre} est pair.")
else:
    print(f"Le nombre {nombre} est impair.")
