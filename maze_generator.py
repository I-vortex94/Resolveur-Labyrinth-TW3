import random
from constants import WALL, EMPTY, Coord

class MazeGenerator:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def generate(self) -> tuple[list[list[int]], Coord, Coord]:
        # on crée une grille vide
        grid = [[WALL for _ in range(self.width)] for _ in range(self.height)]
        start, finish = (0, 1), (self.width - 1, self.height - 2)
        
        def is_valid(x, y):
            return 1 <= x < self.width - 1 and 1 <= y < self.height - 1 and grid[y][x] == WALL
        
        to_explore = [start]
        
        while to_explore:
            x, y = to_explore[-1]
            neighbors = []
            directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if is_valid(nx, ny):
                    neighbors.append((nx, ny))
                        
            if neighbors:
                nx, ny = random.choice(neighbors)
                grid[ny][nx] = EMPTY
                grid[(y + ny) // 2][(x + nx) // 2] = EMPTY
                to_explore.append((nx, ny))
            else:
                to_explore.pop()

        # on vérifie que l'entrée et la sortie sont vides
        grid[start[1]][start[0]] = EMPTY
        
        grid[finish[1]][finish[0]] = EMPTY

        return grid, start, finish