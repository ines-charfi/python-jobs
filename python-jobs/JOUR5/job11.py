# Créer la liste L
Liste = [7, 11, 42, 39, 2]
print("Ma liste avant modification est :  ", Liste)

# Parcourir chaque élément de la liste avec une boucle 'for' mais modifier directement la liste
for i in range(len(Liste)):
    Liste[i] += 1  # Ajouter 1 à chaque élément de la liste

# Afficher la liste modifiée
print("Ma liste après modification est la suivante :", Liste)
