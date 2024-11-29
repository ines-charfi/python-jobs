# Définir la fonction qui ajoute "mangue" à l'index 2 de la liste des fruits
def ajout_mangue():
    # Créer la liste des fruits
    fruits = ["pomme", "cerise", "orange", "melon"]
    print("Ma liste est :", fruits)
    
    # Ajouter "mangue" à l'index 2 en utilisant le slicing
    fruits = fruits[:2] + ["mangue"] + fruits[2:]
    
    # Afficher la liste après l'ajout
    print(fruits)

# Appeler la fonction pour ajouter "mangue" et afficher la liste
ajout_mangue()

