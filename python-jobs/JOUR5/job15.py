def arrondir_et_trier(liste):
    # Étape 1 : Arrondir les nombres
    arrondis = []
    for num in liste:
        # Vérifier si la partie décimale est >= 0.5
        if num - int(num) >= 0.5:
            arrondis.append(int(num) + 1)  # Arrondir vers le haut
        else:
            arrondis.append(int(num))  # Arrondir vers le bas
    
    # Étape 2 : Trier les nombres manuellement
    for i in range(len(arrondis)):
        for j in range(i + 1, len(arrondis)):
            if arrondis[i] > arrondis[j]:
                # Échanger les éléments pour les trier
                temp = arrondis[i]
                arrondis[i] = arrondis[j]
                arrondis[j] = temp
    
    return arrondis

# Liste d'exemple
liste = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

# Appel de la fonction
resultat = arrondir_et_trier(liste)

# Affichage du résultat
print(resultat)
