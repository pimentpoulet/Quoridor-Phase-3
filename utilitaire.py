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
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--parties', action='store_true',
     help='Lister les parties existantes')
    parser.add_argument('-l', '--local', action='store_true',
     help='Jouer en local')
    parser.add_argument('idul', help='IDUl du joueur')

    return parser.parse_args()

def formater_les_parties(parties):
    """Formater une liste de parties
    L'ordre rester exactement la même que ce qui est passé en paramètre.
    Args:
        parties (list): Liste des parties
    Returns:
        str: Représentation des parties
    """
    chaine = ''
    num = 1
    for i in parties:
        ligne = str(num) + ' : ' + i['date'] + ', ' + i['joueurs'][0] + ' vs ' + i['joueurs'][1]
        if i['gagnant'] is None:
            ligne = ''.join([ligne, '\n'])
        else:
            ligne = ''.join([ligne, ', gagnant: ', i['gagnant'], '\n'])
        chaine += ligne
        num += 1
    return chaine

#    x = ''
#    count = 1
#
#    for partie in parties:
#
#        if partie['gagnant'] is None:
#            a = f"{count} : {partie['date']}, {partie['joueurs'][0]} vs {partie['joueurs'][1]}\n"
#
#            x += a
#
#        else:
#            a = f"{count} : {partie['date']}, {partie['joueurs'][0]} vs {partie['joueurs'][1]},"
#            b = f" {partie['gagnant']}\n"
#
#            x += a + b
#        count += 1
#
#    return x
