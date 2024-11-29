#demander au utukisateur de saisir un langage
langage=input("saisir un langage de votre choix : ")

#defintion de la fonction verif_langage
def verif_langage(langage):
    if langage == "javascript":
       print("« tu es un développeur web »")
    elif langage == "python":
       print("« tu es undéveloppeur IA »")
    elif langage == "java":
       print("« tu es un développeur logiciel »")
    elif langage == "reactjs":
       print("« tu es un développeur mobile »")
    else:
        print("« un jour, je serai le meilleur développeur... »")
#appeler la fonction verif_langage
verif_langage(langage)

          
       
    