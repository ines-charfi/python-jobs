# Liste d'origine
Liste = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
print("Ma liste avant modificiation est :  ", Liste)

# Supprimer les doublons en convertissant la liste en ensemble puis la reconvertir en liste
Liste_unique = list(set(Liste))

# Afficher la liste sans doublons
print(Liste_unique)
