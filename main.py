from maze_generator import MazeGenerator
from maze import Maze

def main() -> None:
    width, height = 20, 20
    maze_generator = MazeGenerator(width, height)
    grid, start, finish = maze_generator.generate()
    maze = Maze(grid, start, finish)
    print(maze)

if __name__ == "__main__":
    main()