"""Jeu Quoridor

Ce programme permet de joueur au jeu Quoridor.
"""
from api import débuter_partie, jouer_coup, lister_parties
from quoridor import Quoridor
from utilitaire import analyser_commande, formater_les_parties

# Mettre ici votre secret récupéré depuis le site de PAX
SECRET = "f9ee39b5-284b-4512-a48b-1afd5b3df259"

if __name__ == "__main__":
    args = analyser_commande()
    if args.parties:
        parties = lister_parties(args.idul, SECRET)
        print(formater_les_parties(parties))
    else:
        x = Quoridor(['joueur1', 'joueur2'])
        if args.local:
            # Implémenter la boucle pour jouer contre votre bot en local

            while True:
                print(x)
                valeur = x.récupérer_le_coup(1)

                if valeur[0] == 'D':
                    x.déplacer_jeton(1, [valeur[1][0], valeur[1][1]])
                elif valeur[0] == 'MH':
                    x.placer_un_mur(1, [valeur[1][0], valeur[1][1]], 'horizontal')
                elif valeur[0] == 'MV':
                    x.placer_un_mur(1, [valeur[1][0], valeur[1][1]], 'vertical')

#                print(x)
                valeur_b = x.jouer_le_coup(2)

                if valeur_b[0] == 'D':
                    x.déplacer_jeton(2, [valeur_b[1][0], valeur_b[1][1]])
                elif valeur_b[0] == 'MH':
                    x.placer_un_mur(2, [valeur_b[1][0], valeur_b[1][1]], 'horizontal')
                elif valeur_b[0] == 'MV':
                    x.placer_un_mur(2, [valeur_b[1][0], valeur_b[1][1]], 'vertical')

                if x.est_terminée() is False:
                    continue
                print(f'Le gagnant de la partie est : {x.est_terminée()}')
                break

        else:
            # Implémenter la boucle pour jouer contre le bot du serveur
            id_partie, état = débuter_partie(args.idul, SECRET)
            while True:
                y = Quoridor(état['joueurs'], état['murs'])
                # Afficher la partie
                print(y.formater_légende())
                print(y.formater_damier())
                # Demander au joueur de choisir son prochain coup
                type_coup, position = y.récupérer_le_coup(1)
                # Envoyez le coup au serveur
                id_partie, état = jouer_coup(id_partie, type_coup, position, args.idul, SECRET)
