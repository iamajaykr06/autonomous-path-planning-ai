<p align="center">
  <img src="assets/banner.png" alt="Autonomous Path Planning AI Banner" width="800"/>
</p>

<h1 align="center">🤖 Autonomous Path Planning AI</h1>

<p align="center">
  <strong>A Python framework for building intelligent autonomous navigation systems on 2D grid worlds.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white" alt="Python 3.8+"/>
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License"/>
  <img src="https://img.shields.io/badge/Status-Early_Development-orange.svg" alt="Status"/>
  <img src="https://img.shields.io/badge/PRs-Welcome-brightgreen.svg" alt="PRs Welcome"/>
</p>

---

## 📖 Overview

**Autonomous Path Planning AI** is a modular Python framework designed to simulate and develop intelligent pathfinding algorithms for autonomous agents navigating 2D grid-based environments. The project provides a clean, extensible foundation for experimenting with classic and AI-driven path planning strategies — from A\* search and Dijkstra to reinforcement learning agents.

Whether you're learning about pathfinding algorithms, building a robotics simulator, or prototyping autonomous navigation, this project gives you a structured starting point with a well-defined environment model, flexible obstacle generation, and clear module boundaries for future expansion.

---

## ✨ Features

- **🏛️ Grid World Environment** — A fully customizable 2D grid map with support for start/goal positions, walkable cells, and wall obstacles
- **🧱 Flexible Obstacle Generation** — Three built-in modes for creating environments:
  - **Manual** — Specify exact wall positions for curated test scenarios
  - **Random** — Procedurally generate walls with configurable density and reproducible seeds
  - **Pattern** — Create structured maze-like corridors or scattered block formations
- **🧭 4-Directional Movement** — Agents navigate using up, down, left, right movements with proper boundary and collision checking
- **🖥️ Terminal Visualization** — Built-in ASCII grid renderer for quick debugging and demonstration
- **🔌 Modular Architecture** — Clean separation of concerns across `environment`, `agent`, `planning`, `simulation`, and `evaluation` modules for easy extension

---

## 🏗️ Project Structure

```
autonomous-path-planning-ai/
├── main.py                          # Entry point — demo script
├── requirements.txt                 # Python dependencies
├── assets/                          # Images and media assets
│   ├── banner.png                   # Project banner
│   └── grid_demo.png                # Grid visualization demo
│
├── environment/                     # Grid world modeling
│   ├── __init__.py
│   ├── grid_map.py                  # 2D grid representation (GridMap class)
│   └── obstacle_generator.py        # Wall generation (manual, random, pattern)
│
├── agent/                           # 🚧 Autonomous AI agent (planned)
│   └── __init__.py
│
├── planning/                        # 🚧 Path planning algorithms (planned)
│   └── __init__.py
│
├── simulation/                      # 🚧 Simulation engine (planned)
│   └── __init__.py
│
└── evaluation/                      # 🚧 Metrics & evaluation (planned)
    └── __init__.py
```

> 🚧 Modules marked with 🚧 are planned for future development. See [Roadmap](#-roadmap) for details.

---

## 🚀 Quick Start

### Prerequisites

- **Python 3.8+** installed
- No external dependencies required (uses only Python standard library)

### Installation

```bash
# Clone the repository
git clone https://github.com/iamajaykr06/autonomous-path-planning-ai.git

# Navigate to the project directory
cd autonomous-path-planning-ai

# (Optional) Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Run the Demo

```bash
python main.py
```

### Expected Output

```
========================================
  MODE 1: Manual Walls
========================================
+------------------------------+
| S  .  .  .  .  .  .  .  .  . |
| .  .  .  .  .  .  .  .  .  . |
| .  .  . ### .  .  .  .  .  . |
| .  .  . ### .  .  .  .  .  . |
| .  .  . ### .  .  .  .  .  . |
| .  .  . ############ .  .  . |
| .  .  . ### .  .  .  .  .  . |
| .  .  .  .  .  .  .  .  .  . |
| .  .  .  .  .  .  .  .  .  . |
| .  .  .  .  .  .  .  .  .  G |
+------------------------------+

========================================
  MODE 2: Random Walls (density=0.25)
========================================
+------------------------------+
| S  . ### . ### .  .  . ### . |
|###### . ###### .  . ### .  . |
|### .  .  . ### .  . ###### . |
| .  .  .  .  .  .  .  .  .  . |
| .  . ###### . ######### .  . |
| .  . ### .  .  .  . ### . ###|
| .  .  .  .  .  .  . ###### . |
| . ### .  .  .  .  .  .  .  . |
|### .  .  .  .  . ### .  . ###|
|###### .  .  . ### .  .  .  G |
+------------------------------+

========================================
  MODE 3: Pattern Walls (maze_like)
========================================
+------------------------------+
| S  .  . ### .  . ### .  .  . |
| .  .  . ### .  . ### .  .  . |
| .  .  . ### .  .  .  .  .  . |
| .  .  . ### .  . ### .  .  . |
| .  .  . ### .  . ### .  .  . |
| .  .  .  .  .  . ### .  .  . |
| .  .  . ### .  . ### .  .  . |
| .  .  . ### .  . ### .  .  . |
| .  .  . ### .  . ### .  .  . |
| .  .  . ### .  . ### .  .  G |
+------------------------------+

 S = Start | G = Goal | ### = Wall
```

---

## 📚 Usage Guide

### Creating a Grid Map

```python
from environment.grid_map import GridMap

# Create a 10x10 grid
gmap = GridMap(rows=10, cols=10)

# Set start and goal positions
gmap.set_start(0, 0)   # Top-left corner
gmap.set_goal(9, 9)    # Bottom-right corner

# Add walls manually
gmap.set_wall(2, 3)
gmap.set_wall(3, 3)
gmap.set_wall(4, 3)

# Check if a cell is walkable
is_free = gmap.is_walkable(1, 1)   # True
is_free = gmap.is_walkable(2, 3)   # False (wall)

# Get walkable neighbors of a cell
neighbors = gmap.get_neighbors(0, 0)  # e.g., [(1, 0), (0, 1)]

# Display the grid in the terminal
gmap.print_grid()
```

### Generating Obstacles

#### Mode 1 — Manual Walls

Specify exact wall positions for precise control over the environment layout:

```python
from environment.grid_map import GridMap
from environment.obstacle_generator import ObstacleGenerator

gmap = GridMap(rows=10, cols=10)
gmap.set_start(0, 0)
gmap.set_goal(9, 9)

gen = ObstacleGenerator(gmap)
gen.add_manual_walls([
    (2, 3), (3, 3), (4, 3), (5, 3), (6, 3),  # Vertical wall
    (5, 4), (5, 5), (5, 6),                   # Horizontal extension
])
```

#### Mode 2 — Random Walls

Procedurally scatter walls with configurable density and reproducible seeds:

```python
gen = ObstacleGenerator(gmap)

# 20% of cells become walls, deterministic with seed=42
gen.add_random_walls(density=0.2, seed=42)

# 30% density for a harder challenge
gen.add_random_walls(density=0.3)
```

| Density | Difficulty | Description |
|---------|-----------|-------------|
| `0.1`   | Easy      | Sparse obstacles, many open paths |
| `0.2`   | Medium    | Moderate obstacle density (default) |
| `0.3`   | Hard      | Dense obstacles, limited routing options |

#### Mode 3 — Pattern Walls

Generate structured environments with realistic corridor layouts:

```python
gen = ObstacleGenerator(gmap)

# Maze-like corridors with gaps to pass through
gen.add_pattern_walls(pattern="maze_like")

# Scattered 2x2 wall blocks
gen.add_pattern_walls(pattern="blocks")
```

### Grid Legend

| Symbol | Meaning       | Description                    |
|--------|---------------|--------------------------------|
| ` S `  | Start         | Robot's starting position      |
| ` G `  | Goal          | Target destination             |
| `###`  | Wall          | Impassable obstacle            |
| ` . `  | Empty         | Walkable free space            |

---

## 🧠 Core Concepts

### Cell Types

The grid uses integer constants to represent each cell state:

```python
EMPTY = 0   # Free space — robot can traverse
WALL  = 1   # Blocked — robot cannot enter
START = 2   # Robot's initial position
GOAL  = 3   # Target destination
```

### Movement Model

The agent uses **4-directional (von Neumann) movement** — it can move one cell at a time in the cardinal directions:

```
        Up (-1, 0)
          |
Left ←  [X]  → Right
 (0, -1)   (0, +1)
          |
       Down (+1, 0)
```

### Architecture Design

```
┌──────────────────────────────────────────────────────┐
│                    main.py (Entry)                   │
└────────────┬────────────────────────────┬────────────┘
             │                            │
     ┌───────▼────────┐          ┌────────▼───────┐
     │   Environment   │          │   ObstacleGen   │
     │   (GridMap)     │◄─────────│                 │
     └───────┬────────┘          └────────────────┘
             │
     ┌───────▼────────┐
     │    Agent        │  ← (Planned)
     │ (AI Navigator)  │
     └───────┬────────┘
             │
     ┌───────▼────────┐
     │   Planning      │  ← (Planned)
     │ (Path Algo)     │
     └───────┬────────┘
             │
     ┌───────▼────────┐
     │  Simulation     │  ← (Planned)
     │ (Run & Visual)  │
     └───────┬────────┘
             │
     ┌───────▼────────┐
     │  Evaluation     │  ← (Planned)
     │ (Metrics & QA)  │
     └────────────────┘
```

---

## 🗺️ Roadmap

### ✅ Completed

- [x] Grid world environment (`GridMap` class) with cell types and movement
- [x] Terminal-based grid visualization
- [x] Manual obstacle placement
- [x] Random obstacle generation with density control and seed support
- [x] Pattern-based obstacle generation (maze-like corridors, block formations)

### 🚧 In Progress

- [ ] **Path Planning Algorithms** (`planning/`)
  - [ ] A\* Search Algorithm
  - [ ] Dijkstra's Algorithm
  - [ ] BFS (Breadth-First Search)
  - [ ] Greedy Best-First Search
  - [ ] Comparison of algorithm performance

### 📋 Planned

- [ ] **Autonomous AI Agent** (`agent/`)
  - [ ] Reinforcement Learning agent (Q-Learning)
  - [ ] Rule-based heuristic agent
  - [ ] Configurable agent behaviors

- [ ] **Simulation Engine** (`simulation/`)
  - [ ] Step-by-step agent movement simulation
  - [ ] Visual animation of the pathfinding process
  - [ ] Real-time environment interaction

- [ ] **Evaluation & Metrics** (`evaluation/`)
  - [ ] Path length optimization analysis
  - [ ] Computational cost benchmarking
  - [ ] Success rate across random environments
  - [ ] Comparative algorithm scoring

- [ ] **Enhanced Visualization**
  - [ ] Matplotlib/Pygame graphical grid display
  - [ ] Animated path traversal
  - [ ] Color-coded algorithm comparison view

- [ ] **Advanced Features**
  - [ ] 8-directional movement support
  - [ ] Weighted terrain (different movement costs)
  - [ ] Dynamic obstacles (moving barriers)
  - [ ] Multi-agent pathfinding

---

## 🤝 Contributing

Contributions are welcome! This project is in early development, making it a great time to shape its direction.

### How to Contribute

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/your-feature-name`)
3. **Commit** your changes (`git commit -m 'Add your feature description'`)
4. **Push** to the branch (`git push origin feature/your-feature-name`)
5. **Open** a Pull Request

### Contribution Ideas

- Implement a pathfinding algorithm (A\*, Dijkstra, BFS)
- Add a new obstacle pattern generator
- Build a graphical visualization layer
- Create evaluation benchmarks
- Add unit tests for existing modules
- Implement the AI agent module

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Inspired by classic pathfinding and autonomous navigation research
- Built as an educational tool for understanding grid-based AI systems
- Grid world design patterns from robotics and game AI literature

---

<p align="center">
  Built with 🧠 by <a href="https://github.com/iamajaykr06">iamajaykr06</a>
</p>
