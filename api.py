"""Module d'API du jeu Quoridor

Attributes:
    URL (str): Constante représentant le début de l'url du serveur de jeu.

Functions:
    * lister_parties - Récupérer la liste des parties reçus du serveur.
    * débuter_partie - Créer une nouvelle partie et retourne l'état de cette dernière.
    * récupérer_partie - Retrouver l'état d'une partie spécifique.
    * jouer_coup - Exécute un coup et retourne le nouvel état de jeu.
"""
import requests

URL = "https://pax.ulaval.ca/quoridor/api/v2/"

def débuter_partie(idul, secret):
    """Débuter une partie

    Args:
        idul (str): idul du joueur
        secret (str): secret récupérer depuis le site de PAX

    Raises:
        PermissionError: Erreur levée lorsque le serveur retourne un code 401.
        RuntimeError: Erreur levée lorsque le serveur retourne un code 406.
        ConnectionError: Erreur levée lorsque le serveur retourne un code autre que 200, 401 ou 406

    Returns:
        tuple: Tuple constitué de l'identifiant de la partie en cours
            et de l'état courant du jeu, après avoir décodé
            le JSON de sa réponse.
    """
    rep = requests.post(URL+'partie', auth=(idul, secret))

    if rep.status_code == 200:
        rep=rep.json()
        return (rep['id'], rep['état'])

    if rep.status_code == 401:
        rep=rep.json()
        raise PermissionError(rep['message'])

    if rep.status_code == 406:
        rep=rep.json()
        raise RuntimeError(rep['message'])

    raise ConnectionError()


def récupérer_partie(id_partie, idul, secret):
    """Récupérer une partie

    Args:
        id_partie (str): identifiant de la partie à récupérer
        idul (str): idul du joueur
        secret (str): secret récupérer depuis le site de PAX

    Raises:
        PermissionError: Erreur levée lorsque le serveur retourne un code 401.
        RuntimeError: Erreur levée lorsque le serveur retourne un code 406.
        ConnectionError: Erreur levée lorsque le serveur retourne un code autre que 200, 401 ou 406

    Returns:
        tuple: Tuple constitué de l'identifiant de la partie en cours
            et de l'état courant du jeu, après avoir décodé
            le JSON de sa réponse.
    """
    rep = requests.get(URL+id_partie, auth=(idul, secret))

    if rep.status_code == 200:
        rep=rep.json()
        return (rep['id'], rep['état'], rep['gagnant'])

    if rep.status_code == 401:
        rep=rep.json()
        raise PermissionError(rep['message'])

    if rep.status_code == 406:
        rep=rep.json()
        raise RuntimeError(rep['message'])

    raise ConnectionError()


def jouer_coup(id_partie, type_coup, position, idul, secret):
    """Jouer un coup

    Args:
        id_partie (str): Identifiant de la partie.
        type_coup (str): Type de coup du joueur :
                            'D' pour déplacer le jeton,
                            'MH' pour placer un mur horizontal,
                            'MV' pour placer un mur vertical;
        position (list): La position [x, y] du coup.
        idul (str): idul du joueur
        secret (str): secret récupérer depuis le site de PAX

    Raises:
        StopIteration: Erreur levée lorsqu'il y a un gagnant dans la réponse du serveur.
        PermissionError: Erreur levée lorsque le serveur retourne un code 401.
        RuntimeError: Erreur levée lorsque le serveur retourne un code 406.
        ConnectionError: Erreur levée lorsque le serveur retourne un code autre que 200, 401 ou 406

    Returns:
        tuple: Tuple constitué de l'identifiant de la partie en cours
            et de l'état courant du jeu, après avoir décodé
            le JSON de sa réponse.
    """
    rep = requests.put(URL+'jouer', auth=(idul, secret), json={'id': id_partie,
    'type': type_coup, 'pos': position})

    if rep.status_code == 200:
        rep=rep.json()
        if rep['gagnant'] is not None:
            raise StopIteration(rep['gagnant'])
        return (rep['id'], rep['état'])

    if rep.status_code == 401:
        rep=rep.json()
        raise PermissionError(rep['message'])

    if rep.status_code == 406:
        rep=rep.json()
        raise RuntimeError(rep['message'])

    raise ConnectionError()
