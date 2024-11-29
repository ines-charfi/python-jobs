# Déclaration des variables
nom_produit = "T-shirt"
prix_unitaire = 20.0  # Prix du produit
quantite_en_stock = 100  # Quantité du produit en stock

# Afficher les informations initiales du produit
print("Avant l'achat et l'inflation:")
print("Produit:", nom_produit)
print("Prix:", prix_unitaire, "€")
print("Stock:", quantite_en_stock)
print("------------------------------")

# Demander à l'utilisateur combien de produits il veut acheter
quantite_achetee = int(input(f"Combien de {nom_produit}s voulez-vous acheter ? "))

# Vérifier si il y a assez de stock
if quantite_achetee <= quantite_en_stock:
    quantite_en_stock -= quantite_achetee  # Mettre à jour le stock
    print(f"Vous avez acheté {quantite_achetee} {nom_produit}(s).")
else:
    print("Désolé, il n'y a pas assez de stock.")
    quantite_en_stock = 0  # Mettre le stock à 0 si tout est épuisé

# Appliquer l'inflation (augmentation du prix de 10%)
prix_unitaire = prix_unitaire * 1.10  # Augmenter le prix de 10%

# Afficher les informations après l'achat et l'inflation
print("\nAprès l'achat et l'inflation:")
print("Produit:", nom_produit)
print("Prix après inflation:", round(prix_unitaire, 2), "€")
print("Stock restant:", quantite_en_stock)
