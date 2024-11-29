# Afficher tous les nombres premiers jusqu'à 1000
for n in range(2, 1001):  # On commence à 2, car 1 n'est pas un nombre premier
    # Vérifier si n est divisible par un nombre entre 2 et n-1
    for i in range(2, n):
        if n % i == 0:  # Si n est divisible par i, ce n'est pas un nombre premier
            break  
    else:
        # Si on n'a pas trouvé de diviseur, n est un nombre premier
        print(n)

