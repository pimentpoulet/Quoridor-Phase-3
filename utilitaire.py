"""Module de fonctions utilitaires pour le jeu jeu Quoridor

Functions:
    * analyser_commande - Génère un interpréteur de commande.
"""
import argparse


def analyser_commande():
    """Génère un interpréteur de commande.

    Returns:
        Namespace: Un objet Namespace tel que retourné par `parser.parse_args()`.
                    Cet objet a trois attributs: « idul » représentant l'idul
                    du joueur, « parties » qui est un booléen `True`/`False`
                    et « local » qui est un booléen `True`/`False`.
    """
    parser = argparse.ArgumentParser(description="Jeu Quoridor - phase 3")
    parser.add_argument('-a', '--automatique', action = 'store_true', 
    help='Activer le mode automatique')
    parser.add_argument('-x', "--graphique", action='store_true', help='Activer le mode graphique')
    parser.add_argument('idul', help='IDUL du joueur')

    return parser.parse_args()
