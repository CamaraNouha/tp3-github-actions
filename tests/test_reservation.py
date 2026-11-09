import pytest
from app.reservation import Reservation, Stock
# Fixture : crée un nouveau stock de 5 unités
@pytest.fixture
def stock():
    return Stock(5)

# Test 1 : réservation réussie de 2 unités
def test_reservation_confirmee(stock):
    reservation = Reservation(stock)
    resultat = reservation.reserver(2)
    assert resultat == "confirmee"
    assert stock.quantite == 3

# Test 2 : réservation refusée de 6 unités
def test_reservation_refusee(stock):
    reservation = Reservation(stock)
    resultat = reservation.reserver(6)
    assert resultat == "refusee"
    assert stock.quantite == 5
# Test 3 : réservation de la totalité du stock
def test_reservation_stock_total(stock):
    reservation = Reservation(stock)
    resultat = reservation.reserver(5)
    assert resultat == "confirmee"
    assert stock.quantite == 0
# Test 4 : réservation d'une quantité nulle
def test_reservation_quantite_zero(stock):
    reservation = Reservation(stock)
    with pytest.raises(ValueError):
        reservation.reserver(0)

    assert stock.quantite == 5