#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from Screen import Screen
from Spot import Spot
from PathFinder import PathFinder
import pygame


def main():
    cols, rows = 10, 10
    screen = Screen(400, 400, rows)
    screen.show()
    screen.makeGrid()
    
    grid = [[Spot(screen, i, j) for j in range(0, rows)] for i in range(0, cols)]

    """grid = []
    for i in range(0, cols):
        preList = []
        for j in range(0, rows):
            preList.append(Spot(screen, i, j))
        grid.append(preList)            
    """
    for i in range(0, cols):
        for j in range(0, rows):
            grid[i][j].addNeigbors(grid, cols, rows)

    start = grid[0][0]
    stop = grid[cols - 1][rows - 1]

    pathFinder = PathFinder(grid, start, stop)
    
    while True:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                screen.close()
        
        
        result = pathFinder.findPath()
        pathFinder.showOpenSet()
        pathFinder.showPath()
        screen.update()
            
    
if __name__ == "__main__":
    main()