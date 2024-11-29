# demander à l'utlisateur de saisir les deux nombres
num1 = int(input("Saisir le premier nombre : "))
operator= input("saisir un oprérateur (+, -, *, /, %) :  ")
num2 = int(input("Saisir le deuxième nombre :  "))


#définir la fonction calcule
def calcule(num1, operator, num2):
     if operator == "+":
        return  print (num1 + num2)
  
     elif operator == "-":
         return print (num1 - num2)
     
     elif operator == "*":
         return print(num1 * num2)
     
     elif operator =="/":
          if num2!= 0:
            return print (num1 / num2)
          else: 
            return print("Erreur divison par 0")
     elif operator == "%" :
       return print(num1 % num2)
     else:
        return print("operator invalide")
        
        #résultat
resultat = calcule(10, '+', 5)
print(resultat) 