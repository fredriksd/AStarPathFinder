from Screen import Screen 
from random import random
import pygame

class Spot:
    def __init__(self, screen, i, j):
        self.screen     = screen
        self.i          = i
        self.j          = j
        self.neighbors  = []
        

    def show(self, color):
        if (self.i == 0 and self.j == 0):
            self.screen.updateGrid(self.i, self.j, pygame.Color("green"))
        self.screen.updateGrid(self.i, self.j, color)

    def addNeigbors(self, grid, cols, rows):
        i = self.i
        j = self.j
        if (i < cols - 1):
            self.neighbors.append(grid[i + 1][j])
        if (i > 0):
            self.neighbors.append(grid[i - 1][j])
        if (j < rows - 1):
            self.neighbors.append(grid[i][j + 1])
        if (j > 0):
            self.neighbors.append(grid[i][j - 1])
        if (i > 0 and j > 0):
            self.neighbors.append(grid[i - 1][j - 1])
        if (i < cols - 1 and j > 0):
            self.neighbors.append(grid[i + 1][j - 1])
        if (i > 0 and j < rows - 1):
            self.neighbors.append(grid[i - 1][j + 1])
        if (i < cols - 1 and j < rows - 1):
            self.neighbors.append(grid[i + 1 ][j + 1])
        
