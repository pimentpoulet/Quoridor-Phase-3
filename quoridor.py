"""Module de la classe Quoridor

Classes:
    * Quoridor - Classe pour encapsuler le jeu Quoridor.
"""
from copy import deepcopy
from quoridor_error import QuoridorError
from graphe import construire_graphe
import networkx as nx

class Quoridor:
    """Classe pour encapsuler le jeu Quoridor.

    Vous ne devez pas créer d'autre attributs pour votre classe.

    Attributes:
        état (dict): état du jeu tenu à jour.
    """
    def __init__(self, joueurs, murs=None):
        """Constructeur de la classe Quoridor.

        Initialise une partie de Quoridor avec les joueurs et les murs spécifiés,
        en s'assurant de faire une copie profonde de tout ce qui a besoin d'être copié.

        Appel la méthode `vérification` pour valider les données et assigne
        ce qu'elle retourne à l'attribut `self.état`.

        Cette méthode ne devrait pas être modifiée.

        Args:
            joueurs (List): un itérable de deux joueurs dont le premier est toujours celui qui
                débute la partie.
            murs (Dict, optionnel): Un dictionnaire contenant une clé 'horizontaux' associée à
                la liste des positions [x, y] des murs horizontaux, et une clé 'verticaux'
                associée à la liste des positions [x, y] des murs verticaux.
        """
        self.état = deepcopy(self.vérification(joueurs, murs))


    def vérification(self, joueurs, murs=None):
        """Vérification d'initialisation d'une instance de la classe Quoridor.

        Valide les données arguments de construction de l'instance et retourne
        l'état si valide.

        Args:
            joueurs (List): un itérable de deux joueurs dont le premier est toujours celui qui
                débute la partie.
            murs (Dict, optionnel): Un dictionnaire contenant une clé 'horizontaux' associée à
                la liste des positions [x, y] des murs horizontaux, et une clé 'verticaux'
                associée à la liste des positions [x, y] des murs verticaux.
        Returns:
            Dict: Une copie de l'état actuel du jeu sous la forme d'un dictionnaire.
                Notez que les positions doivent être sous forme de list [x, y] uniquement.
        Raises:
            QuoridorError: L'argument 'joueurs' n'est pas itérable.
            QuoridorError: L'itérable de joueurs en contient un nombre différent de deux.
            QuoridorError: Le nombre de murs qu'un joueur peut placer est plus grand que 10,
                            ou négatif.
            QuoridorError: La position d'un joueur est invalide.
            QuoridorError: L'argument 'murs' n'est pas un dictionnaire lorsque présent.
            QuoridorError: Le total des murs placés et plaçables n'est pas égal à 20.
            QuoridorError: La position d'un mur est invalide.
        """
        # Test 1 : vérifie que les joueurs sont un dict ou un str
        try:
            iter(joueurs)
        except TypeError:
            raise QuoridorError('L\'argument \'joueurs\' n\'est pas itérable.')

        # Test 2 : longueur différente de 2
        if len(joueurs) != 2:
            raise QuoridorError('L\'itérable de joueurs en contient un nombre différent de deux.')

        # Si murs vaut None, on crée un nouveau dictionnaire de murs
        if murs is None:
            murs = {"horizontaux": [], "verticaux": []}

        # Test 4 : argument murs
        if murs is not None and not isinstance(murs, dict):
            raise QuoridorError('L\'argument \'murs\' n\'est pas un dictionnaire.')

        # Si le joueur 1 est un string, on crée un nouveau joueur sous forme de dictionnaire
        if isinstance(joueurs[0], str):
            joueurs[0] = {'nom':joueurs[0], 'pos':[5, 1], 'murs':10}

        # Si le joueur 2 est un string, on crée un nouveau joueur sous forme de dictionnaire
        if isinstance(joueurs[1], str):
            joueurs[1] = {'nom':joueurs[1], 'pos':[5, 9], 'murs':10}

        # Test 3 : Nombre de murs qu'un joueur peut placer ou position joueur invalide
        for element in joueurs:
            if isinstance(element, dict):
                if len(murs['verticaux']) > 0 and len(murs['horizontaux']) > 0:
                    if element['pos'] in murs['verticaux'] or element['pos'] in murs['horizontaux']:
                        #raise QuoridorError('La position d\'un joueur est invalide.')
                        pass
                    if element['murs'] < 0 or element['murs'] > 10:
                        raise QuoridorError(
                            "Le nombre de murs qu'un joueur peut placer est plus grand que 10 ou négatif."
                            )

        # Test 6 : Total murs
        if joueurs[0]['murs'] + joueurs[1]['murs'] + len(
            murs['horizontaux']) + len(murs['verticaux'])!= 20:
            raise QuoridorError('Le total des murs placés et plaçables n\'est pas égal à 20.')

        # Test 7 : position mur invalide
        for i in murs['horizontaux']:
            if i[0] >= 9:
                raise QuoridorError('La position d\'un mur est invalide.')
            if i[1] > 9:
                raise QuoridorError('La position d\'un mur est invalide.')
        for i in murs['verticaux']:
            if i[0] > 9:
                raise QuoridorError('La position d\'un mur est invalide.')
            if i[1] >= 9:
                raise QuoridorError('La position d\'un mur est invalide.')

        # Crée l'état de jeu avec les données
        gamestate = {"joueurs": [joueurs[0], joueurs[1]], "murs": murs}

        return gamestate


    def formater_légende(self):
        """Formater la représentation graphique de la légende.

        Returns:
            str: Chaîne de caractères représentant la légende.
        """
        if len(self.état['joueurs'][0]['nom']) >= len(self.état['joueurs'][1]['nom']):
            c_1 = 1
            c_2 = len(self.état['joueurs'][0]['nom']) - len(self.état['joueurs'][1]['nom']) + 1
        else:
            c_1 = len(self.état['joueurs'][1]['nom']) - len(self.état['joueurs'][0]['nom']) + 1
            c_2 = 1

        légende_1 = f"Légende:\n   1={self.état['joueurs'][0]['nom']},{c_1*' '}murs={self.état['joueurs'][0]['murs']*'|'}\n"

        légende_2 = f"   2={self.état['joueurs'][1]['nom']},{c_2*' '}murs={self.état['joueurs'][1]['murs']*'|'}\n"

        return légende_1 + légende_2


    def formater_damier(self):
        """Formater la représentation graphique du damier.

        Returns:
            str: Chaîne de caractères représentant le damier.
        """
        damier_de_base = ['   -----------------------------------\n']

        for i in range(9, 0, -1):
            damier_de_base.append(f"{i} | .   .   .   .   .   .   .   .   . |\n")
            damier_de_base.append('  |                                   |\n')
        damier_de_base = damier_de_base[: -1]
        damier_de_base.append('--|-----------------------------------\n')
        damier_de_base.append('  | 1   2   3   4   5   6   7   8   9\n')


    # Placer les joueurs :
    # Inverser le damier pour inverser l'indice des lignes :

        damier_de_base.reverse()


    # Modifier les lignes :

        liste_ligne = list(damier_de_base[2 * self.état['joueurs'][0]['pos'][1]])
        liste_ligne[4 * self.état['joueurs'][0]['pos'][0]] = '1'
        damier_de_base[2 * self.état['joueurs'][0]['pos'][1]] = ''.join(liste_ligne)

        liste_ligne = list(damier_de_base[2 * self.état['joueurs'][1]['pos'][1]])
        liste_ligne[4 * self.état['joueurs'][1]['pos'][0]] = '2'
        damier_de_base[2 * self.état['joueurs'][1]['pos'][1]] = ''.join(liste_ligne)


    # Placer les murs :
    # Murs horizontaux :

        for murs_h in self.état['murs']['horizontaux']:

            ligne_h_1 = damier_de_base[(2 * murs_h[1]) - 1][0:((4 * murs_h[0]) - 1)] + (7 * '-')
            ligne_h_1 = ligne_h_1 + damier_de_base[(2 * murs_h[1]) - 1][(4 * murs_h[0]) + 6:]
            damier_de_base[(2 * murs_h[1]) - 1] = ligne_h_1

    # Murs verticaux :

        for murs_v in self.état['murs']['verticaux']:

            ligne_v1_1 = damier_de_base[2 * murs_v[1]][0:(4 * murs_v[0]) - 2]
            ligne_v1_1 = ligne_v1_1 + '|' + damier_de_base[2*murs_v[1]][(4 * murs_v[0]) - 1:]
            damier_de_base[2 * murs_v[1]] = ligne_v1_1

            ligne_v2_1 = damier_de_base[(2 * murs_v[1]) + 1][0:(4 * murs_v[0]) - 2]
            ligne_v2_1 = ligne_v2_1 + '|' + damier_de_base[(2*murs_v[1]) + 1][(4 * murs_v[0]) - 1:]
            damier_de_base[(2 * murs_v[1]) + 1] = ligne_v2_1

            ligne_v3_1 = damier_de_base[(2 * murs_v[1]) + 2][0:(4 * murs_v[0]) - 2]
            ligne_v3_1 = ligne_v3_1 + '|' + damier_de_base[(2*murs_v[1]) + 2][(4 * murs_v[0]) - 1:]
            damier_de_base[(2 * murs_v[1]) + 2] = ligne_v3_1

        damier = ''
        damier_de_base.reverse()

        for ligne in damier_de_base:
            damier += ligne

        return damier


    def __str__(self):
        """Représentation en art ascii de l'état actuel de la partie.

        Cette représentation est la même que celle du projet précédent.

        Returns:
            str: La chaîne de caractères de la représentation.
        """
        #print('tabarnak')
        return f"{self.formater_légende()}{self.formater_damier()}"


    def état_courant(self):
        """Produire l'état actuel du jeu.

        Cette méthode ne doit pas être modifiée.

        Returns:
            Dict: Une copie de l'état actuel du jeu sous la forme d'un dictionnaire.
                Notez que les positions doivent être sous forme de liste [x, y] uniquement.
        """
        return deepcopy(self.état)


    def est_terminée(self):
        """Déterminer si la partie est terminée.

        Returns:
            str/bool: Le nom du gagnant si la partie est terminée; False autrement.
        """
        # JOUEUR 1 :

        if self.état['joueurs'][0]['pos'][1] == 9:
            return self.état['joueurs'][0]['nom']

        # JOUEUR 2 :

        if self.état['joueurs'][1]['pos'][1] == 1:
            return self.état['joueurs'][1]['nom']

        #  SI PAS DE GAGNANT :
        return False


    def récupérer_le_coup(self, joueur):
        """Récupérer le coup

        Notez que seul 2 questions devrait être posée à l'utilisateur.

        Notez aussi que cette méthode ne devrait pas modifier l'état du jeu.

        Args:
            joueur (int): Un entier spécifiant le numéro du joueur (1 ou 2).

        Raises:
            QuoridorError: Le numéro du joueur est autre que 1 ou 2.
            QuoridorError: Le type de coup est invalide.
            QuoridorError: La position est invalide (en dehors du damier).

        Returns:
            tuple: Un tuple composé d'un type de coup et de la position.
            Le type de coup est une chaîne de caractères.
            La position est une liste de 2 entier [x, y].
        """
        #Test du numero du joueur
        if joueur not in [1,2]:
            raise QuoridorError('Le numéro du joueur est autre que 1 ou 2.')


        # Input du type de coup

        type_coup = input('Quel type de coup voulez-vous jouer? (\'D\', \'MH\', \'MV\') ?')
        #if (tp == 'D') or (tp == 'MH') or (tp == 'MV')

        if (type_coup in ['D', 'MH', 'MV']):
            pass
        else:
            raise QuoridorError('Le type de coup est invalide.')


    # Input de la position

        position = input('Donnez la position où appliquer ce coup (x,y) :').split(',')

        if len(position) == 2 and isinstance(int(position[0]), int) and isinstance(int(position[1]),
            int) and 1 <= int(position[0]) <= 9 and 1 <= int(position[1]) <= 9:
            pass
        else:
            raise QuoridorError('La position est invalide (en dehors du damier).')

        return (type_coup, [int(position[0]), int(position[1])])


    def déplacer_jeton(self, joueur, position):
        """Déplace un jeton.

        Pour le joueur spécifié, déplacer son jeton à la position spécifiée.

        Args:
            joueur (int): Un entier spécifiant le numéro du joueur (1 ou 2).
            position (List[int, int]): La liste [x, y] de la position du jeton (1<=x<=9 et 1<=y<=9).

        Raises:
            QuoridorError: Le numéro du joueur est autre que 1 ou 2.
            QuoridorError: La position est invalide (en dehors du damier).
            QuoridorError: La position est invalide pour l'état actuel du jeu.
        """
        # On crée un tuple de la position actuelle du joueur
        p = tuple(self.état['joueurs'][joueur-1]['pos'])

        # On génère un graphe
        graphe = construire_graphe([self.état['joueurs'][0]['pos'], self.état['joueurs'][1]['pos']],
        self.état['murs']['horizontaux'], self.état['murs']['verticaux'])

        # Test du numero de joueur
        if joueur not in (1, 2):
            raise QuoridorError('Le numéro du joueur est autre que 1 ou 2.')

        # Test de la position (dans le damier)
        if position[0] > 9 or position[1] > 9 or position[0] < 1 or position[1] < 1:
            raise QuoridorError('La position est invalide (en dehors du damier)')

        # Si la position est valide, on assigne au joueur sa nouvelle position
        #print(list(graphe.successors(p)))
        #print(tuple(position))
        if tuple(position) in list(graphe.successors(p)):
            self.état['joueurs'][joueur-1]['pos'] = position
        else:
            raise QuoridorError("La position est invalide pour l'état actuel du jeu.")


    def placer_un_mur(self, joueur, position, orientation):
        """Placer un mur.

        Pour le joueur spécifié, placer un mur à la position spécifiée.

        Args:
            joueur (int): le numéro du joueur (1 ou 2).
            position (List[int, int]): la liste [x, y] de la position du mur.
            orientation (str): l'orientation du mur ('horizontal' ou 'vertical').

        Raises:
            QuoridorError: Le numéro du joueur est autre que 1 ou 2.
            QuoridorError: Un mur occupe déjà cette position.
            QuoridorError: La position est invalide pour cette orientation.
            QuoridorError: Le joueur a déjà placé tous ses murs.
        """
        # Test du numero du joueur
        if joueur not in (1, 2):
            raise QuoridorError('Le numéro du joueur est autre que 1 ou 2.')

        # Test des murs du joueur
        if self.état['joueurs'][joueur-1]['murs'] == 0:
            raise QuoridorError('Le joueur a déjà placé tous ses murs.')

        #Test de l'orientation et de la position du mur
        taken = []
        for i in self.état['murs']['horizontaux']:
            taken.append(i)
            taken.append([i[0]+1, i[1]])
        for j in self.état['murs']['verticaux']:
            taken.append(j)
            taken.append([j[0], j[1]+1])

        if orientation == 'horizontal':
            p1 = position
            p2 = [position[0]+1, position[1]]
            if position in self.état['murs']['horizontaux']:
                raise QuoridorError('Un mur occupe déjà cette position.')
            if p1 in taken or p2 in taken or 1 > position[0] > 8:
                raise QuoridorError('La position est invalide pour cette orientation.')
            # On ajoute un mur horizontal au jeu si sa position est acceptée
            self.état['murs']['horizontaux'].append(position)
        elif orientation == 'vertical':
            p1 = position
            p2 = [position[0], position[1]+1]
            if position in self.état['murs']['verticaux']:
                raise QuoridorError('Un mur occupe déjà cette position.')
            if p1 in taken or p2 in taken or 1 > position[1] > 8:
                raise QuoridorError('La position est invalide pour cette orientation.')
            # On ajoute un mur vertical au jeu si sa position est acceptée
            self.état['murs']['verticaux'].append(position)

        # A supprimer si code fonctionnel
        #if orientation == 'horizontal':
            #p1 = position
            #p2 = [position[0]+1, position[1]]
            #if p1 in taken or p2 in taken or 1 > position[0] > 8:
            #    raise QuoridorError('La position est invalide pour cette orientation.')
        #elif orientation == 'vertical':
            #p1 = position
            #p2 = [position[0], position[1]+1]
            #if p1 in taken or p2 in taken or 1 > position[1] > 8:
                #raise QuoridorError('La position est invalide pour cette orientation.')

        # Si toutes les conditions sont passées, on enlève un mur au joueur
        self.état['joueurs'][joueur-1]['murs'] -= 1


    def jouer_le_coup(self):
        """Jouer un coup automatique pour un joueur.

        Pour le joueur spécifié, jouer automatiquement son meilleur coup pour l'état actuel
        de la partie. Ce coup est soit le déplacement de son jeton, soit le placement d'un
        mur horizontal ou vertical.


        Raises:
            QuoridorError: La partie est déjà terminée.
            QuoridorError: Le robot est enfermé

        Returns:
            Tuple[str, List[int, int]]: Un tuple composé du type et de la position du coup joué.
        """
        meilleur_type = ''
        meilleure_pos = []

        # Construit le graphe du jeu
        graphe = construire_graphe([self.état['joueurs'][0]['pos'],
        self.état['joueurs'][1]['pos']], self.état['murs']['horizontaux'],
        self.état['murs']['verticaux'])

        # Crée le shortest path pour chaque joueur
        sp_1 = list(nx.shortest_path(graphe, tuple(self.état['joueurs'][0]['pos']), "B1"))
        sp_2 = list(nx.shortest_path(graphe, tuple(self.état['joueurs'][1]['pos']), "B2"))
        print('shortest path j1 :', sp_1)
        print('shortest path j2 :', sp_2)

        # Contruit une liste des positions occupées par les murs
        murs_h = []
        murs_v = []
        for i in self.état['murs']['horizontaux']:
            murs_h.append(i)
            murs_h.append([i[0]+1, i[1]])
        for j in self.état['murs']['verticaux']:
            murs_v.append(j)
            murs_v.append([j[0], j[1]+1])
        taken = murs_h + murs_v
        nb_murs = self.état['joueurs'][1]['murs']
        
        #taken = []
        #for i in self.état['murs']['horizontaux']:
        #    taken.append(i)
        #    taken.append([i[0]+1, i[1]])
        #for j in self.état['murs']['verticaux']:
        #    taken.append(j)
        #    taken.append([j[0], j[1]+1])

        # Test si le robot est enfermé
        if len(sp_2) == 1:
            raise QuoridorError('Le robot est enfermé')

        # Test pour une partie terminée
        if self.est_terminée is False:
            raise QuoridorError('La partie est déjà terminée.')


        # Si le shortest path du joueur est plus petit que celui du robot, déplacement selon le shortest path

        # Sinon, si shortest path du robot = déplacement vertical, on met un mur horziontal
        if sp_2[1][1] != sp_2[0][1] and nb_murs > 0 and len(sp_2) < len(sp_1) and len(sp_2) <= 7:
            for i in sp_2[1:]:
                print(i)
                print(murs_h)
                print(taken)
                if [i[0], i[1]+1] not in murs_h and [i[0]+1, i[1]+1] not in taken and i[0] < 9 and i[0] >= 1 and i[1] <= 8:
                    if i[0] == 9:
                        meilleur_type = 'MH'
                        meilleure_pos = [i[0]-1, i[1]+1]
                        break
                    else: 
                        meilleur_type = 'MH'
                        meilleure_pos = [i[0], i[1]+1]
                        break

        # Sinon, si shortest path du robot = déplacement horizontal, on met un mur vertical
        elif sp_2[1][0] != sp_2[0][0] and nb_murs > 0 and len(sp_2) < len(sp_1) and len(sp_2) <= 5:
            for i in sp_2[1:]:
                print(i)
                print(murs_v)
                print(taken)
                if [i[0]+1, i[1]] not in murs_v and [i[0]+1, i[1]+1] not in taken and i[1] < 9 and i[1] >= 1 and i[0] <= 8:
                    meilleur_type = 'MV'
                    meilleure_pos = [i[0]+1, i[1]]
                    break
        else:
            meilleur_type = 'D'
            meilleure_pos = list(sp_1[1])

        return (meilleur_type, meilleure_pos)
