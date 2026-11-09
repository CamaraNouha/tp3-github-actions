from app.texte import nettoyer_texte
import pytest
"""
def test_nettoyer_texte():
    assert nettoyer_texte("BONJOUR monde") == "bonjour monde"

def test_nettoyer_texte2():
    assert nettoyer_texte("déjà propre") == "déjà propre"



@pytest.mark.parametrize(
    "texte, expected",
    [
        ("BONJOUR monde", "bonjour monde"),
        ("déjà propre", "déjà propre"),
        ("   ", ""),
        ("", "")
    ]
)
def test_nettoyer_texte(texte, expected):
    assert nettoyer_texte(texte) == expected



#3
"""
def test_nettoyer_texte_type_error_123():
    with pytest.raises(TypeError):
        nettoyer_texte(123)

def test_nettoyer_texte_type_error_none():
    with pytest.raises(TypeError):
        nettoyer_texte(None)