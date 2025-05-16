import random

def genmaze(x, y):
    maze = [['#' for _ in range(y)] for _ in range(x)]  # Create a grid filled with walls

    # Carve out a maze using a simple randomized depth-first search
    def carve_passages(cx, cy):
        directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 < nx < x - 1 and 0 < ny < y - 1 and maze[nx][ny] == '#':
                maze[cx + dx // 2][cy + dy // 2] = ' '  # Remove wall between cells
                maze[nx][ny] = ' '  # Mark the new cell as part of the maze
                carve_passages(nx, ny)

    # Start carving from the top-left corner
    maze[1][1] = ' '
    carve_passages(1, 1)

    # Add entrance and exit
    maze[0][1] = ' '  # Entrance at the top
    maze[x - 1][y - 2] = ' '  # Exit at the bottom

    return maze

def printmaze(maze):
    for row in maze:
        print(' '.join(row))
