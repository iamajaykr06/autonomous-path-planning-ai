# main.py
# Entry point — we'll keep adding to this each day.

from environment.grid_map import GridMap

# Create a 10x10 grid
grid_map = GridMap(rows=10, cols=10)

# Set start and goal
grid_map.set_start(0, 0)
grid_map.set_goal(9, 9)

# Add some walls manually for today
for r in range(2, 7):
    grid_map.set_wall(r, 4)   # vertical wall
for c in range(4, 8):
    grid_map.set_wall(5, c)   # horizontal wall

# Print it
print("\n🗺️  Grid World — Day 1\n")
grid_map.print_grid()
print("\n S = Robot Start | G = Goal | ### = Wall\n")
