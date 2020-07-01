from Screen import Screen 

class Spot:
    def __init__(self, screen, ):
        self.screen = screen

    def show(self):
        self.screen.updateGrid()