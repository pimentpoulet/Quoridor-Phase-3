"""Jeu Quoridor

Ce programme permet de joueur au jeu Quoridor.
"""
import turtle
from api import débuter_partie, jouer_coup
from quoridor import Quoridor
from utilitaire import analyser_commande
import networkx as nx

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
            try:
                #print('dans le 1er try')
                type_coup, position = game.jouer_le_coup()
                id_partie, état = jouer_coup(id_partie, type_coup, position, args.idul, SECRET)
            except (PermissionError, RuntimeError):
                try:
                    print('dans le 2e try')
                    type_coup = 'D'
                    position = list(nx.shortest_path(game.graphe, tuple(game.état['joueurs'][0]['pos']), "B1"))[1]
                    #print(type_coup, position)
                    id_partie, état = jouer_coup(id_partie, type_coup, position, args.idul, SECRET)
                except (StopIteration):
                    #print('2e exception')
                    game.est_terminée()
                    break
            except (StopIteration):
                #print('3e exception')
                game.est_terminée()
                break
                
                
                
                #print('dans le except')
                #try:
                #    type_coup = 'D'
                #    position = list(nx.shortest_path(game.graphe, tuple(game.état['joueurs'][0]['pos']), "B1"))[1]
                #    id_partie, état = jouer_coup(id_partie, type_coup, position, args.idul, SECRET)
                #except:
                #    print('dans le  2e except')
                #    break
                #print('dans le except')
                #print(game.état['joueurs'][0]['pos'], game.état['joueurs'][1]['pos'])
                #if game.état['joueurs'][1]['pos'][1] == 1:
                #    print('je break')
                #    break
                #else:
                #    print('Je deplace')
                #    type_coup = 'D'
                #    position = list(nx.shortest_path(game.graphe, tuple(game.état['joueurs'][0]['pos']), "B1"))[1]
                #    id_partie, état = jouer_coup(id_partie, type_coup, position, args.idul, SECRET)
            #print(type_coup, position)
            # Envoyer le coup au serveur
            #id_partie, état = jouer_coup(id_partie, type_coup, position, args.idul, SECRET)
    elif args.graphique:
    # Mode manuel avec affichage
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
game = Quoridor(état)

