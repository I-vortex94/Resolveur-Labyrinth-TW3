import random
from typing import List, Tuple
from constants import Coord

class MazeGenerator:
    """
    Génère un labyrinthe complet, avec un départ et une arrivée
    """
    def __init__(self, width: int, height; int) -> None:
        """
        Génère matrice de mur
        """
        if width % 2 == 0: #Avoir une longueur impaire
            width += 1
        if height % 2 == 0: #Avoir une hauteur impaire
            height += 1
        self.width: int = width #longeur du laby
        self.height: int = height #hauteur du laby

    def generate(self) -> Tuple[List[List[bool]]], Tuple[Coord, Coord]: #Pour faire le laby
        """
        Placer le départ (D)
        """
        # Créer une matrice de murs (False) et de passages (True)
        maze: List[List[bool]] = [[False for _ in range(self.width)] for _ in range(self.height)]

        start_x: int = random.randrange(1, self.width - 1, 2) # 2 pour s'assurer qu'il ne tombe pas sur un bord
        start_y: int = random.randrange(1, self.height - 1, 2) # 2 pour s'assurer qu'il ne tombe pas sur un bord
        self.maze[start_y][start_x] = True #Place le départ sur le laby : True
    
        #On défini les directions possibles pour les neighbors (haut, bas, gauche, droite)
        directions: List[Coord] = [(-2, 0), (2, 0), (0, -2), (0, 2)]

        to_explore: List[Coord] = [(start_x, start_y)] # Initialisation (nan c pas une récurrence...) pour générer un laby faisable

        """
        Générer le laby
        """
        while to_explore:
            x, y = to_explore[-1] #Prend la dernière cellule
            neighbors: List[Coord] = [] #On va lister les neighbors de cette cellule dans... une liste

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 1 <= nx < self.width - 1 and 1 <= ny < self.height - 1: #Sécurité pour vérif qu'on est bien dans les bordures et que c bien un mur
                    if self.maze[ny][nx] == '#': 
                        neighbors.append((nx, ny))

            if neighbors: #Permet de vérifier s'il a des neighbors murs, miskin s'il en a pas, lol
                nx, ny = random.choice(neighbors) #C assez explicite je pense
                self.maze[ny][nx] = ' ' #Transformer le mur en passage
                self.maze[(y + ny) // 2][(x + nx) // 2] = ' ' #Lier la cellule avec la voisine choisit, bah oui on comptait de 2 en 2...
                to_explore.append((nx, ny))
            else:
                to_explore.pop() #enlève le dernier élément de la liste a explorer et refait si aucun voisin mur
        
        """
        Mettre une bordure
        """
        for i in range(self.width):
            self.maze[0][i] = '#'
            self.maze[self.height - 1][i] = '#'
        for i in range(self.height):
            self.maze[i][0] = '#'
            self.maze[i][self.width - 1] = '#'
    
        """
        Mettre l'arrivée (A)
        """
        end_x: int = random.randrange(1, self.width, 2)
        end_y: int = random.randrange(1, self.height, 2)
        while self.maze[end_y][end_x] != ' ': #Pour ne pas avoir l'arrivée sur un mur, ca serait balo. Mais plutôt sur un des chemins qu'on a crée plus tôt
            end_x = random.randrange(1, self.width, 2)
            end_y = random.randrange(1, self.height, 2)
        self.maze[end_y][end_x] = 'A' #Marqué l'arrivée

    def display(self, maze: List[List[bool]]) -> None:
        """
        Affiche le laby
        """
        for row in maze:
          print(''.join(['#' if not cell esle ' ' for cell in row))

width: int = 31 #Mettre des nombres impaires
height: int = 41 #Mettre des nombres impaires
# (Parce que ça fait 3141 : 3,141)
maze = MazeGenerator(width, height)

maze.generate()
maze.display()
