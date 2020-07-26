
from user import Printer
import time

from dude import dude
from space import space
class game():
    def __init__(self,height,width,players):
        self.sleep = False
        self.height = height
        self.width = width
        self.map = create_map(height,width)
        self.rebels = []
        self.players = players
        self.bullets = []
        for i in range(players):
            self.rebels.append(dude(self,1,i*100,10,i))
        for i in range(self.width):
            self.map[self.height-3][i] = space('-',full = True)
            
    def round(self):
        for bullet in self.bullets:
            if bullet.active:
                bullet.move()
        for reb in self.rebels:
            reb.move()
        #Printer(self,self.map,self.height,self.width) 

         
def create_map(height,width):
    map = []
    for row in range(height):
        map.append([])
        for col in range(width):
            map[row].append(space(' '))
    return map
