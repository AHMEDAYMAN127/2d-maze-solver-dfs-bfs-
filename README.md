his Python application reads and solves mazes using BFS (Breadth-First Search) and DFS (Depth-First Search) algorithms. The maze is loaded from a .txt file and displayed visually using Tkinter. The solution can be animated step by step to show how the path is discovered.

How it works:

Maze Input: The maze is stored in a .txt file. Each character represents a cell:

'A' → Starting point of the maze

'B' → Goal (end point)

' ' → Open space that can be traversed

Any other character → Wall/obstacle

Walls: Represented internally as True in a 2D list, so the algorithms know which cells cannot be moved into.

Start and Goal: Stored as coordinates (row, column) to guide the search algorithms.

Features:

Load mazes from .txt files of any size.

Solve using BFS (guarantees the shortest path) or DFS (explores deep paths first).

Step-by-step animation to visualize the path being found.

Automatic scaling of the maze to fit the window.

Technologies Used:

Python 3

Tkinter for GUI

Collections (deque) for BFS/DFS implementation
