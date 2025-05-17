import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from MazeOfTerror.model.maze_terror import Laberinto
primer_laberinto = Laberinto(2)
print(primer_laberinto.matriz)