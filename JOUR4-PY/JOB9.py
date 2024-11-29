# Demander à l'utilisateur de saisir trois notes
note1 = float(input("Entrez la première note : "))  # Demande la première note
note2 = float(input("Entrez la deuxième note : "))  # Demande la deuxième note
note3 = float(input("Entrez la troisième note : "))  # Demande la troisième note
#définition de la fonction moyenne
def moyenne(note1, note2, note3):
 return (note1 + note2 + note3)/3
moyenne_etudiant = moyenne(note1, note2, note3)    
if moyenne_etudiant >= 15 and moyenne_etudiant <= 20:
         print("Très bon élève")
elif moyenne_etudiant >= 11 and moyenne_etudiant < 15:
         print("Bon élève")
elif moyenne_etudiant >= 8 and moyenne_etudiant < 11:
         print("Élève moyen")
else:
        print("Élève devant faire des efforts")
    