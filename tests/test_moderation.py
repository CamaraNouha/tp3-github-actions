import pytest
from unittest.mock import Mock
from app.moderation import decider

# Test 1 : le modèle retourne spam
def test_decider_spam():
    # Arrange
    modele = Mock()
    modele.predict.return_value = "spam"
    # Act
    resultat = decider(modele, "Offre miracle")
    # Assert
    assert resultat == "bloquer"
    modele.predict.assert_called_once_with("Offre miracle")


# Test 2 : le modèle retourne normal
def test_decider_normal():
    # Arrange
    modele = Mock()
    modele.predict.return_value = "normal"
    # Act
    resultat = decider(modele, "Bonjour, comment allez-vous ?")
    # Assert
    assert resultat == "autoriser"
    modele.predict.assert_called_once_with(
        "Bonjour, comment allez-vous ?"
    )



def test_decider_erreur():
    # Arrange
    modele = Mock()
    modele.predict.side_effect = RuntimeError("Modele indisponible")

    # Act & Assert
    with pytest.raises(RuntimeError, match="Modele indisponible"):
        decider(modele, "Offre miracle")