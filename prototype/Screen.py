import pygame
import sys

class Screen:
    def __init__(self, width, height, rowsCols):
        self.size = width, height
        self.rowsCols = rowsCols
        self.screen = pygame.display.set_mode(self.size)
        pygame.init()

    def show(self):
        black = (0, 0, 0)
        self.screen.fill(black)   
        pygame.display.flip()
    
    def makeGrid(self):
        w, h = self.size[0]/self.rowsCols, self.size[1]/self.rowsCols
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                pygame.draw.rect(self.screen, pygame.Color("white"), 
                                 pygame.rect.Rect(i*w, j*h, w-1, h-1), 1)
        self.update()

    def updateGrid(self, i, j, colour):
        w, h = self.size[0]/self.rowsCols, self.size[1]/self.rowsCols
        pygame.draw.rect(self.screen, colour,
                        pygame.rect.Rect(i*w, j*h, w-1, h-1))

    def close(self):
        sys.exit()

    def update(self):
        pygame.display.flip()