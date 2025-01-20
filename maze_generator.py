from random import randint
from constants import WALL, EMPTY, Coord

class MazeGenerator:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def generate(self) -> tuple[list[list[int]], Coord, Coord]:
        # on crée une grille vide
        grid = [[EMPTY for _ in range(self.width)] for _ in range(self.height)]
        start, finish = (0, 0), (self.width - 1, self.height - 1)
        
        # Implémentationn ici
        
        # ---

        # on vérifie que l'entrée et la sortie sont vides
        grid[start[1]][start[0]] = EMPTY
        grid[finish[1]][finish[0]] = EMPTY

        return grid, start, finish