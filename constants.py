from typing import Tuple

# Coord est un alias pour un tuple de deux entiers représentant une coordonnée (x, y)
Coord = Tuple[int, int]

# Définition d'un alias pour le type des cases dans le labyrinthe
State = bool

# Valeurs associées aux murs et espaces
EMPTY: State = True
WALL: State = False

# Constantes pour la taille du labyrinthe
DEFAULT_WIDTH = 62
DEFAULT_HEIGHT = 51