# main.py
from environment.grid_map import GridMap
from environment.obstacle_generator import ObstacleGenerator

print("=" * 40)
print("  MODE 1: Manual Walls")
print("=" * 40)
gmap1 = GridMap(rows=10, cols=10)
gmap1.set_start(0, 0)
gmap1.set_goal(9, 9)
gen1 = ObstacleGenerator(gmap1)
gen1.add_manual_walls([
    (2,3),(3,3),(4,3),(5,3),(6,3),
    (5,4),(5,5),(5,6),
])
gmap1.print_grid()

print("\n" + "=" * 40)
print("  MODE 2: Random Walls (density=0.25)")
print("=" * 40)
gmap2 = GridMap(rows=10, cols=10)
gmap2.set_start(0, 0)
gmap2.set_goal(9, 9)
gen2 = ObstacleGenerator(gmap2)
gen2.add_random_walls(density=0.25, seed=42)
gmap2.print_grid()

print("\n" + "=" * 40)
print("  MODE 3: Pattern Walls (maze_like)")
print("=" * 40)
gmap3 = GridMap(rows=10, cols=10)
gmap3.set_start(0, 0)
gmap3.set_goal(9, 9)
gen3 = ObstacleGenerator(gmap3)
gen3.add_pattern_walls(pattern="maze_like")
gmap3.print_grid()

print("\n S = Start | G = Goal | ### = Wall\n")