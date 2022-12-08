"""Jeu Quoridor

Ce programme permet de joueur au jeu Quoridor.
"""
import turtle
from api import débuter_partie, jouer_coup
from quoridor import Quoridor
from utilitaire import analyser_commande

# Mettre ici votre secret récupéré depuis le site de PAX
SECRET = "f9ee39b5-284b-4512-a48b-1afd5b3df259"

if __name__ == "__main__":
    x = Quoridor(['joueur1', 'joueur2'])
    args = analyser_commande()
    if args.automatique:
    # Mode automatique sans affichage
        pass
    elif args.graphique:
    # Mode manuel avec affichage
        pass
    elif args.automatique and args.graphique:
    # Mode automatique avec affichage
        pass
    else:
        pass
    # Mode par défaut : manuel, sans affichage
        # Implémenter la boucle pour jouer contre le bot du serveur
        id_partie, état = débuter_partie(args.idul, SECRET)
        while True:
            y = Quoridor(état['joueurs'], état['murs'])
            # Afficher la partie
            print(y.formater_légende())
            print(y.formater_damier())
            # Demander au joueur de choisir son prochain coup
            type_coup, position = y.récupérer_le_coup(1)
            # Envoyer le coup au serveur
            id_partie, état = jouer_coup(id_partie, type_coup, position, args.idul, SECRET)
