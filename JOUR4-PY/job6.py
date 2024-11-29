#demander au utilisateur de saisir un nombre
nombre= int(input("Saisir un nombre : "))
#définition de la fonction positivité ()
def positivité(nombre):
    if nombre > 0:
         print("le nombre est positif")
    elif nombre < 0:
         print("le nombre est négatif")
    else:
         print("le nombre est égal à 0")
     
#appeler la fonction positivité
positivité(nombre)