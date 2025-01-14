from maze import MazeGenerator
from constants import DEFAULT_WIDTH, DEFAULT_HEIGHT

def main() -> None:
    """
    Fonction principale pour générer et afficher le labyrinthe.
    """
    # Créer un générateur de labyrinthe avec les dimensions par défaut
    maze_generator = MazeGenerator(DEFAULT_WIDTH, DEFAULT_HEIGHT)
    
    # Générer le labyrinthe et obtenir l'entrée et la sortie
    maze, (start, end) = maze_generator.generate()

    # Afficher le labyrinthe
    maze_generator.display(maze)

    # Afficher les positions de l'entrée et de la sortie
    print(f"Entrée: {start}")
    print(f"Sortie: {end}")

if __name__ == "__main__":
    main()
