"""Tests Quoridor

Ce module contient des tests unitaires pour le projet Quoridor.
"""
from copy import deepcopy

from quoridor import Quoridor


def test_créer_état_pour_une_nouvelle_partie():
    """
    Test de la fonction
    """

    état = {
        "joueurs": [
            {"nom": "Robin", "murs": 10, "pos": [5, 1]},
            {"nom": "Alfred", "murs": 10, "pos": [5, 9]},
        ],
        "murs": {
            "horizontaux": [],
            "verticaux": [],
        },
    }
    attendu = deepcopy(état)

    résultat = Quoridor(attendu["joueurs"]).état_courant()

    assert attendu == résultat, "Échec du test de création d'état pour une nouvelle partie"


def test_créer_état_pour_une_partie_avancée():
    """
    Test de la fonction
    """
    état = {
        "joueurs": [
            {"nom": "Alfred", "murs": 7, "pos": [5, 5]},
            {"nom": "Robin", "murs": 3, "pos": [8, 6]},
        ],
        "murs": {
            "horizontaux": [[4, 4], [2, 6], [3, 8], [5, 8], [7, 8]],
            "verticaux": [[6, 2], [4, 4], [2, 6], [7, 5], [7, 7]],
        },
    }
    attendu = deepcopy(état)

    résultat = Quoridor(attendu["joueurs"], attendu["murs"]).état_courant()

    assert attendu == résultat, "Échec du test de création d'état pour une partie avancée"


def test_afficher_une_nouvelle_partie():
    """
    Test de la fonction
    """
    état = {
        "joueurs": [
            {"nom": "Robin", "murs": 10, "pos": [5, 1]},
            {"nom": "Alfred", "murs": 10, "pos": [5, 9]},
        ],
        "murs": {
            "horizontaux": [],
            "verticaux": [],
        },
    }

    résultat = str(Quoridor(état["joueurs"], état["murs"]))

    attendu = (
        "Légende:\n"
        "   1=Robin,  murs=||||||||||\n"
        "   2=Alfred, murs=||||||||||\n"
        "   -----------------------------------\n"
        "9 | .   .   .   .   2   .   .   .   . |\n"
        "  |                                   |\n"
        "8 | .   .   .   .   .   .   .   .   . |\n"
        "  |                                   |\n"
        "7 | .   .   .   .   .   .   .   .   . |\n"
        "  |                                   |\n"
        "6 | .   .   .   .   .   .   .   .   . |\n"
        "  |                                   |\n"
        "5 | .   .   .   .   .   .   .   .   . |\n"
        "  |                                   |\n"
        "4 | .   .   .   .   .   .   .   .   . |\n"
        "  |                                   |\n"
        "3 | .   .   .   .   .   .   .   .   . |\n"
        "  |                                   |\n"
        "2 | .   .   .   .   .   .   .   .   . |\n"
        "  |                                   |\n"
        "1 | .   .   .   .   1   .   .   .   . |\n"
        "--|-----------------------------------\n"
        "  | 1   2   3   4   5   6   7   8   9\n"
    )

    assert attendu == résultat, "Échec du test d'affichage d'une nouvelle partie"



def test_afficher_une_partie_avancée():
    """
    Test de la fonction
    """
    état = {
        "joueurs": [
            {"nom": "Alfred", "murs": 7, "pos": [5, 5]},
            {"nom": "Robin", "murs": 3, "pos": [8, 6]},
        ],
        "murs": {
            "horizontaux": [[4, 4], [2, 6], [3, 8], [5, 8], [7, 8]],
            "verticaux": [[6, 2], [4, 4], [2, 6], [7, 5], [7, 7]],
        },
    }

    résultat = str(Quoridor(état["joueurs"], état["murs"]))

    attendu = (
        "Légende:\n"
        "   1=Alfred, murs=|||||||\n"
        "   2=Robin,  murs=|||\n"
        "   -----------------------------------\n"
        "9 | .   .   .   .   .   .   .   .   . |\n"
        "  |                                   |\n"
        "8 | .   .   .   .   .   . | .   .   . |\n"
        "  |        ------- -------|-------    |\n"
        "7 | . | .   .   .   .   . | .   .   . |\n"
        "  |   |                               |\n"
        "6 | . | .   .   .   .   . | .   2   . |\n"
        "  |    -------            |           |\n"
        "5 | .   .   . | .   1   . | .   .   . |\n"
        "  |           |                       |\n"
        "4 | .   .   . | .   .   .   .   .   . |\n"
        "  |            -------                |\n"
        "3 | .   .   .   .   . | .   .   .   . |\n"
        "  |                   |               |\n"
        "2 | .   .   .   .   . | .   .   .   . |\n"
        "  |                                   |\n"
        "1 | .   .   .   .   .   .   .   .   . |\n"
        "--|-----------------------------------\n"
        "  | 1   2   3   4   5   6   7   8   9\n"
    )
    assert attendu == résultat, "Échec du test d'affichage d'une partie avancée"


if __name__ == "__main__":
    print("Tests :")
    test_créer_état_pour_une_nouvelle_partie()
    print("✅ test_créer_état_pour_une_nouvelle_partie")
    test_créer_état_pour_une_partie_avancée()
    print("✅ test_créer_état_pour_une_partie_avancée")
    test_afficher_une_nouvelle_partie()
    print("✅ test_afficher_une_nouvelle_partie")
    test_afficher_une_partie_avancée()
    print("✅ test_afficher_une_partie_avancée")
