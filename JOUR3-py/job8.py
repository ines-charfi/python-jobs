# Demander les longueurs des côtés du triangle
a = float(input("Entrez la longueur du côté a : "))
b = float(input("Entrez la longueur du côté b : "))
c = float(input("Entrez la longueur du côté c : "))

# Vérifier si les trois côtés forment un triangle
if a + b > c and a + c > b and b + c > a:
    print("Ces longueurs forment un triangle.")
    
        # Vérifier le type de triangle
    if a == b == c:
        print("Le triangle est équilatéral.")
    elif a == b or a == c or b == c:
        print("Le triangle est isocèle.")

  # Vérifier si ce triangle isocèle est aussi rectangle
        if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            print("Le triangle isocèle est aussi rectangle.")
    else:
        print("Le triangle est quelconque.")
           # Vérifier si ce triangle quelconque est rectangle
        if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            print("Le triangle est rectangle.")
else:
    print("Ces longueurs ne forment pas un triangle.")



