# environment/obstacle_generator.py
# Generates obstacles (walls) on the grid in different ways.

import random


class ObstacleGenerator:
    """
    Adds walls to a GridMap object.
    Supports three modes:
      - manual   : you specify exact wall positions
      - random   : walls placed randomly across the grid
      - pattern  : walls form structured shapes (corridors, blocks)
    """

    def __init__(self, grid_map):
        """
        Args:
            grid_map: a GridMap object (from grid_map.py)
        """
        self.grid_map = grid_map

    # ----------------------------------------------------------
    # MODE 1: Manual — you give exact (row, col) positions
    # ----------------------------------------------------------
    def add_manual_walls(self, wall_positions):
        """
        Place walls at specific positions.

        Args:
            wall_positions: list of (row, col) tuples

        Example:
            generator.add_manual_walls([(2,3), (3,3), (4,3)])
        """
        for (r, c) in wall_positions:
            self.grid_map.set_wall(r, c)

    # ----------------------------------------------------------
    # MODE 2: Random — scatter walls across the grid
    # ----------------------------------------------------------
    def add_random_walls(self, density=0.2, seed=None):
        """
        Randomly place walls across the grid.

        Args:
            density : float between 0.0 and 1.0
                      0.1 = 10% of cells become walls (easy)
                      0.3 = 30% of cells become walls (hard)
            seed    : set a number for reproducible results
                      (same seed = same walls every run)

        Example:
            generator.add_random_walls(density=0.2, seed=42)
        """
        if seed is not None:
            random.seed(seed)

        for r in range(self.grid_map.rows):
            for c in range(self.grid_map.cols):
                # Skip start and goal cells
                if (r, c) == self.grid_map.start:
                    continue
                if (r, c) == self.grid_map.goal:
                    continue
                # Randomly decide if this cell becomes a wall
                if random.random() < density:
                    self.grid_map.set_wall(r, c)

    # ----------------------------------------------------------
    # MODE 3: Pattern — structured walls (more realistic)
    # ----------------------------------------------------------
    def add_pattern_walls(self, pattern="maze_like"):
        """
        Add walls in structured patterns.

        Args:
            pattern: "maze_like" — corridors and barriers
                     "blocks"    — scattered wall blocks

        Example:
            generator.add_pattern_walls(pattern="blocks")
        """
        if pattern == "maze_like":
            self._add_maze_like_walls()
        elif pattern == "blocks":
            self._add_block_walls()

    def _add_maze_like_walls(self):
        """Creates corridor-style walls — like a simple maze."""
        rows = self.grid_map.rows
        cols = self.grid_map.cols

        # Vertical wall with a gap (a corridor to pass through)
        wall_col = cols // 3
        gap_row  = rows // 2          # leave a gap here
        for r in range(rows):
            if r != gap_row:          # skip the gap row
                self.grid_map.set_wall(r, wall_col)

        # Second vertical wall with a different gap
        wall_col2 = (cols * 2) // 3
        gap_row2  = rows // 4
        for r in range(rows):
            if r != gap_row2:
                self.grid_map.set_wall(r, wall_col2)

    def _add_block_walls(self):
        """Creates 2x2 wall blocks scattered across the grid."""
        rows = self.grid_map.rows
        cols = self.grid_map.cols

        # Place blocks every 3 cells, offset rows and cols
        for r in range(1, rows - 1, 3):
            for c in range(1, cols - 1, 3):
                # Skip if too close to start or goal
                if (r, c) == self.grid_map.start:
                    continue
                if (r, c) == self.grid_map.goal:
                    continue
                # Place a 2x2 block
                for dr in range(2):
                    for dc in range(2):
                        self.grid_map.set_wall(r + dr, c + dc)