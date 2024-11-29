# On commence à boucler sur les nombres de 1 à 100
for i in range(1, 101):
    # Vérifie si le nombre est divisible à la fois par 3 et par 5
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")  # Si c'est le cas, afficher "FizzBuzz"
    # Vérifie si le nombre est divisible par 3
    elif i % 3 == 0:
        print("Fizz")  # Si c'est le cas, afficher "Fizz"
    # Vérifie si le nombre est divisible par 5
    elif i % 5 == 0:
        print("Buzz")  # Si c'est le cas, afficher "Buzz"
    else:
        print(i)  # Sinon, afficher le nombre lui-même
