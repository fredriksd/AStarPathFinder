from Screen import Screen
from Spot import Spot
from pygame import Color
from math import sqrt

class PathFinder:
    def __init__(self, screen, grid, start, stop):
        self.screen    = screen
        self.grid      = grid
        self.stop      = stop
        self.openSet   = [start]
        self.closedSet = []
        #self.previous  = []
        self.previous  = {}
        self.fScore    = {start : self.heuristic(start)}
        self.gScore    = {start : 0}
        self.path      = []
        self.found     = False

    """def reconstructPath(self, cameFromSet, currentSpot):
        total_path = [currentSpot]
        for i in range(len(cameFromSet), 0, -1):
            total_path.append(cameFromSet[i])
        return total_path
    """
    def reconstructPath(self, cameFromSet, currentSpot):
        total_path = [currentSpot]
        while currentSpot in cameFromSet.keys():
            currentSpot = cameFromSet[currentSpot]
            total_path.insert(0, currentSpot)
        return total_path

    def dist(self, a, b):
        return sqrt((b.x - a.x)**2 + (b.y - a.y)**2)

    def heuristic(self, spot):
        return self.dist(spot, self.stop)

    def showOpenSet(self):
        for spot in self.openSet:
            spot.show(Color("green"))
    def showPath(self):
        for spot in self.path:
            spot.show(Color("blue"))
    
    def findPath(self):
        if(not self.found):
            while (len(self.openSet) > 0):
                winner = 0
                for i in range(0, len(self.openSet)):
                    if(self.fScore[self.openSet[i]] < self.fScore[self.openSet[winner]]):
                        winner = i
                current = self.openSet[winner]
                if (current == self.stop):                    
                    self.path = self.reconstructPath(self.previous, current)
                    #self.path = self.previous
                    self.found = True
                    self.openSet = []
                    return self.found
                self.openSet.remove(current)
                self.closedSet.append(current)
                        
                neighbors = current.neighbors
                for neighbor in neighbors:
                    if(neighbor not in self.closedSet):
                        if (neighbor not in self.openSet):
                            self.gScore[neighbor] = 1000
                        tempGScore = self.gScore[current] + self.dist(neighbor, current)
                        if(tempGScore < self.gScore[neighbor]):
                            #self.previous.append(current)
                            self.previous[neighbor] = current
                            if (neighbor not in self.openSet):
                                self.openSet.append(neighbor)
                    self.gScore[neighbor] = tempGScore
                    self.fScore[neighbor] = self.gScore[neighbor] + self.heuristic(neighbor)
        return False
