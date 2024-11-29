# Définir la fonction qui ajoute "mangue" à l'index 2 de la liste des fruits
def ajout_mangue():
    # Créer la liste des fruits
    fruits = ["pomme", "cerise", "orange", "melon"]
    
    # Ajouter "mangue" à l'index 2 (avant "orange")
    fruits.insert(2, "mangue")
    
    # Afficher la liste après l'ajout
    print(fruits)

# Appeler la fonction pour ajouter "mangue" et afficher la liste
ajout_mangue()