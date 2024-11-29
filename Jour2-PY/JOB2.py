# On parcourt les nombres de 0 à 20
for i in range(21):  # range(21) génère des nombres de 0 à 20
    if i % 2 == 0:  # Si le nombre est pair (divisible par 2)
        print(i)  # On affiche le nombre
    else:
        print("le nombre ",i, "est impair")
    
