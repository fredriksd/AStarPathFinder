from Screen import Screen 
from random import random
import pygame

class Spot:
    def __init__(self, screen, x, y):
        self.screen     = screen
        self.x          = x
        self.y          = y
        self.neighbors  = []
        

    def show(self, color):
        if (self.x == 0 and self.y == 0):
            self.screen.updateGrid(self.x, self.y, pygame.Color("green"))
        self.screen.updateGrid(self.x, self.y, color)

    def addNeigbors(self, grid, cols, rows):
        x = self.x
        y = self.y
        if (x < cols - 1):
            self.neighbors.append(grid[x + 1][y])
        if (x > 0):
            self.neighbors.append(grid[x - 1][y])
        if (y < rows - 1):
            self.neighbors.append(grid[x][y + 1])
        if (y > 0):
            self.neighbors.append(grid[x][y - 1])