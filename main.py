"""Jeu Quoridor

Ce programme permet de joueur au jeu Quoridor.
"""
import turtle
from api import débuter_partie, jouer_coup
from quoridor import Quoridor
from utilitaire import analyser_commande
#from quoridorx import QuoridorX

# Mettre ici votre secret récupéré depuis le site de PAX
#SECRET = "f9ee39b5-284b-4512-a48b-1afd5b3df259"
# Secret de Chris
SECRET = "493162ca-e829-48c5-9e94-3d43b9497375"

if __name__ == "__main__":
    args = analyser_commande()
    if args.automatique:
    # Mode automatique sans affichage
        id_partie, état = débuter_partie(args.idul, SECRET)
        while True:
            #print(état['joueurs'], état['murs'])
            game = Quoridor(état['joueurs'], état['murs'])
            # Afficher la partie
            print(game)
            # Un buffer de temps
            input('Appuyez sur Enter pour continuer')
            # Le joueur joue son meilleur coup
            type_coup, position = game.jouer_le_coup()
            print(type_coup, position)
            # Envoyer le coup au serveur
            id_partie, état = jouer_coup(id_partie, type_coup, position, args.idul, SECRET)

    elif args.graphique:
        pass
    # Mode manuel avec affichage
        id_partie, état = débuter_partie(args.idul, SECRET)
        while True:
            game = QuoridorX(état['joueurs'], état['murs'])
            # Afficher la partie
            game.afficher()
            
            # Transmettre le coup à jouer

            # Le joueur joue son meilleur coup
            type_coup, position = game.jouer_le_coup()
            print(type_coup, position)
            # Envoyer le coup au serveur
            id_partie, état = jouer_coup(id_partie, type_coup, position, args.idul, SECRET)
            pass
    elif args.automatique and args.graphique:
    # Mode automatique avec affichage
        pass

    else:
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

