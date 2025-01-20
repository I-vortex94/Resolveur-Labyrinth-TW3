from maze_generator import MazeGenerator
from maze import Maze
from constants import DEFAULT_WIDTH, DEFAULT_HEIGHT

def main() -> None:
    print('Pour la taille par défaut, appuyer ENTRER.')
    width = input("Entrer la largeur du Labyrinthe : ")
    if width == "":
        width, height = DEFAULT_WIDTH, DEFAULT_HEIGHT
    else:
        width = int(width)
        height = int(input("Entrer la hauteur du Labyrinthe : "))
        if width % 2 == 1:
            width += 1
        if height % 2 == 0:
            height += 1
    maze_generator = MazeGenerator(width, height)
    grid, start, finish = maze_generator.generate()
    maze = Maze(grid, start, finish)
    print(maze)

if __name__ == "__main__":
    main()