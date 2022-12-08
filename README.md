# Quoridor

<img src="https://python.gel.ulaval.ca/media/notebook/quoridor.png" style="display: block; margin-left: auto; margin-right: auto;" alt="Quoridor" width="50%" height="auto">

## Objectifs

Pour ce deuxième projet, vous aurez à créer une classe pour encapsuler le jeu Quoridor. Vous aurez à réutiliser certains segments de code de votre module `quoridor.py`.

## Prérequis

- [Git](https://git-scm.com/downloads/)
- [Python pour macOS](https://www.python.org/downloads/), [Python pour Windows](https://apps.microsoft.com/store/detail/python-310/9PJPW5LDXLZ5)
- [VS Code](https://code.visualstudio.com/download/)

Avant de télécharger Python ou Git, vous pouvez vérifier s'il est déjà installé sur votre ordinateur depuis un terminal. Notez que pour Python les version 3.9, 3.10, 3.11 seront tous compatible. Donc si vous avez déjà une de ces versions, inutile d'en installer une autre.

### Windows

Depuis le menu démarré, cherchez Powershell et exécuter la commande:

```powershell
python3 --version
```

Ça devrait afficher `Python 3.9.7` avec le numéro de votre version au lieu de `3.9.7`.

Si ça ne fonctionne pas, essayez la commande:

```powershell
python --version
```

Si aucune de ces 2 commandes fonctionnent, vous devez télécharger Python depuis le Microsoft Store.

Pour Git vous pouvez vérifier avec la commande:

```powershell
git --version
```

### MacOS

Depuis Finder, cherchez `Terminal`, ouvrez l'application puis exécuter la commande:

```zsh
python3 --version
```

Ça devrait afficher `Python 3.9.7` avec le numéro de votre version au lieu de `3.9.7`.

N'utilisez **jamais** la commande `python` sans le `3` sur MacOS car il fera référence à Python 2.

## Extension VS Code

Voici la liste des extensions **VS Code** que nous vous conseillons d'ajouter à votre configuration:

- Python (celui de Microsoft)
- GitLens $-$ Git supercharged
- Live Share (_Pour le dépannage en ligne_)
- Live Share Extension Pack (_Pour le dépannage en ligne_)

## Commandes utile

Exécuter les tests que nous vous avons fournis

```bash
python3 tests.py
```

Installer un module externe **Python**:

```bash
pip3 install nom-du-module
```

Sous MacOS il sera important d'utiliser `pip3` et non pas `pip`.

Créer un bundle depuis un terminal:

```bash
git bundle create quoridor.bundle --all
```

Vérifier que le bundle a été créé avec succès:

```bash
git bundle verify quoridor.bundle
```

Ouvrir un bundle:

```bash
git clone quoridor.bundle
```

**N'oubliez pas de supprimer les fichiers créés lors de l'ouverture du bundle pour ne pas vous embourber de fichiers inutiles.**

## Liens utile

- [Aide-mémoire Github Git](https://github.github.com/training-kit/downloads/fr/github-git-cheat-sheet.pdf)
