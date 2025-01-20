from constants import Coord, EMPTY, WALL


class Maze:
    def __init__(self, grid: list[list[int]], start: Coord, finish: Coord):
        self.grid = grid
        self.start = start
        self.finish = finish
        self.width = len(grid[0])  # Largeure du labyrinthe
        self.height = len(grid)    # Longueure du labyrinthe


    def __str__(self) -> str:
        return '\n'.join(
                ''.join('██' if cell == WALL else '  ' for cell in row) for row in self.grid
                )