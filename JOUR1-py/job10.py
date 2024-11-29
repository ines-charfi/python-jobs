# Montant initial de l'investissement et taux de rendement
montant_initial = 10000  # Montant initial en euros
taux_rendement = 5  # Taux de rendement annuel en pourcentage

# Calcul du gain initial
gain_initial = montant_initial * (taux_rendement / 100)
print("Gain initial : ", gain_initial, "€")

# L'investisseur ajoute 5000 € à son capital et le taux augmente de 2%
montant_initial += 5000  # Ajouter 5000 €
taux_rendement += 2  # Augmenter le taux de rendement de 2%

# Nouveau gain après l'augmentation du capital
gain_augmentation = montant_initial * (taux_rendement / 100)
print("Gain après ajout de 5000 € : ", gain_augmentation, "€")

# L'investisseur retire 10% et le taux de rendement baisse de 1%
montant_initial -= montant_initial * 0.10  # Retirer 10% du capital
taux_rendement -= 1  # Diminuer le taux de rendement de 1%

# Gain final après le retrait
gain_final = montant_initial * (taux_rendement / 100)
print("Gain final après retrait de 10% et baisse du taux : ", gain_final, "€")
