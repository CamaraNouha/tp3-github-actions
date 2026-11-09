def frais_livraison(montant):
    if montant < 0:
        raise ValueError("Le montant ne peut pas être négatif.")
    if montant >= 300:
        return 0
    return 25