class Stock:
    def __init__(self, quantite):
        self.quantite = quantite

    def retirer(self, quantite):
        if quantite <= 0:
            raise ValueError("La quantité à retirer doit être supérieure à zéro.")
        if quantite > self.quantite:
            return False  # Pas assez de stock disponible
        self.quantite -= quantite
        return True  # Retrait réussi
    
class Reservation:
    def __init__(self, stock):
        self.stock = stock

    def reserver(self, quantite):
        if self.stock.retirer(quantite):
            return "confirmee"
        return "refusee"