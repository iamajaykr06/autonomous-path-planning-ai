# environment/grid_map.py
# Defines the grid world the robot will navigate in.

# Cell type constants — each cell in the grid is one of these
EMPTY = 0   # Free space — robot can walk here
WALL  = 1   # Blocked — robot cannot enter
START = 2   # Where the robot begins
GOAL  = 3   # Where the robot needs to reach


class GridMap:
    """
    Represents the 2D grid world.
    The grid is a list of lists (rows x cols).
    Each cell holds a value: EMPTY, WALL, START, or GOAL.
    """

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.start = None   # Will store (row, col) of start
        self.goal  = None   # Will store (row, col) of goal
        self.grid  = self._create_empty_grid()

    def _create_empty_grid(self):
        """Build a blank grid filled with EMPTY cells."""
        grid = []
        for r in range(self.rows):
            row = [EMPTY] * self.cols
            grid.append(row)
        return grid

    def set_start(self, r, c):
        """Place the robot's starting position."""
        self.start = (r, c)
        self.grid[r][c] = START

    def set_goal(self, r, c):
        """Place the goal position."""
        self.goal = (r, c)
        self.grid[r][c] = GOAL

    def set_wall(self, r, c):
        """Block a cell — robot cannot pass through."""
        # Don't overwrite start or goal
        if self.grid[r][c] not in (START, GOAL):
            self.grid[r][c] = WALL

    def is_walkable(self, r, c):
        """Check if a cell is within bounds and not a wall."""
        in_bounds = (0 <= r < self.rows) and (0 <= c < self.cols)
        if not in_bounds:
            return False
        return self.grid[r][c] != WALL

    def get_neighbors(self, r, c):
        """
        Return all walkable neighbors of a cell.
        A robot can move Up, Down, Left, Right (4 directions).
        """
        directions = [
            (-1,  0),   # Up
            ( 1,  0),   # Down
            ( 0, -1),   # Left
            ( 0,  1),   # Right
        ]
        neighbors = []
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if self.is_walkable(nr, nc):
                neighbors.append((nr, nc))
        return neighbors

    def print_grid(self):
        """Print the grid in the terminal — useful for debugging."""
        symbols = {
            EMPTY: " . ",
            WALL:  "###",
            START: " S ",
            GOAL:  " G ",
        }
        print("+" + "---" * self.cols + "+")
        for row in self.grid:
            print("|", end="")
            for cell in row:
                print(symbols[cell], end="")
            print("|")
        print("+" + "---" * self.cols + "+")