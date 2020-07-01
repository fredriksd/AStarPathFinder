#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from Screen import Screen
from Spot import Spot
from PathFinder import PathFinder
import pygame


def main():
    cols, rows = 40, 40
    screen = Screen(400, 400, 10)
    screen.show()
    screen.makeGrid()
    
    grid = [[Spot(screen, x, y) for x in range(0, rows)] for y in range(0, cols)]
    
    for i in range(0, len(grid)):
        for j in range(0, len(grid)):
            grid[i][j].addNeigbors(grid, cols, rows)

    start = grid[0][0]
    stop = grid[cols - 1][rows - 1]

    pathFinder = PathFinder(screen, grid, start, stop)
    
    while True:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                screen.close()
        
        pathFinder.showOpenSet()
        result = pathFinder.findPath()
        
        pathFinder.showPath()
        screen.update()
            
    
if __name__ == "__main__":
    main()