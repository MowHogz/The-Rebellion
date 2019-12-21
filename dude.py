import time 
from bullet import bullet
from space import space
class dude(space):
    def __init__(self,game,y,x,health):
        self.full = True
        self.t = '*'
        self.game = game
        self.y = y
        self.x = x
        self.height = 3
        self.width = 2
        self.speed = 1
        self.jump_height = 10
        self.jump_momentum= 0
        self.double_jump = False #indicates if player can make a double jump 
        self.health = health
        self.keys_pressed = []
        self.right = True
    def move(self):
        self.remove_dude()
        buttons = self.keys_pressed[:]
        self.keys_pressed = []
        new_y = self.y
        new_x = self.x
        if 'd' in buttons:
            new_x += self.speed
        elif 'a' in buttons:
            new_x -= self.speed

        if self.can_insert(new_y,new_x):#if player if on direction
            self.y = new_y
            self.x = new_x
        else: 
            new_y = self.y
            new_x = self.x
        self.gravity(buttons)
        self.insert_dude()
        if 'x' in buttons:
            self.shoot()
    def shoot(self):
        if self.right:
            self.game.bullets.append(bullet(self.game,self.y-self.height/2,self.x + self.width, self.speed*2, 1,1))
        else:
            self.game.bullets.append(bullet(self.game,self.y-self.height/2,self.x-1, self.speed*2, 1,1))
    def gravity(self,buttons):
        new_y = self.y
        new_x = self.x
        if 'w' in buttons and self.standing(): #if player pressing up and standing on solid floor
            self.double_jump = True
            self.jump_momentum = self.jump_height
        if self.jump_momentum > 0:
            self.jump_momentum -= self.speed
            new_y -= self.speed
            if self.jump_momentum > 5:
                self.jump_momentum -= self.speed
                new_y -= self.speed
        elif not self.standing():
            new_y += self.speed
        if self.can_insert(new_y,new_x):#if player if on direction
            self.y = new_y
            self.x = new_x
        else:
            new_y = self.y
            new_x = self.x
        pass
    def remove_dude (self):
        for row in range(self.y,self.y + self.height):
            for col in range(self.x, self.x + self.width):
                self.game.map[row][col] = space(' ')
    def insert_dude (self):
        for row in range(self.y,self.y + self.height):
            for col in range(self.x, self.x + self.width):
                self.game.map[row][col] = self
    def standing(self):
        if self.can_insert(self.y + 1, self.x): 
            return False
        return True
    def can_insert(self,y,x): #checks if player can fit y,x
        for row in range(y,y + self.height):
            for col in range(x, x + self.width):
                if self.game.map[row][col].full:
                    return False
        return True
    def damage (self,nezeq):
        self.health -= nezeq 
        if self.health <=0:
            return False
        return True
    def get_hit(self,nezeq,push = 0):
        self.remove_dude()
        if not self.damage(nezeq):
            return False
        if push > 0:
            for pushment in range(push):#start moving as far as player has been pushed
                if self.can_insert(self.y,self.x + 1):
                    self.x += 1
                else:
                    self.insert_dude()
                    return True
        else: 
            for pushment in range(abs(push)):#start moving as far as player has been pushed
                if self.can_insert(self.y,self.x + 1):
                    self.x += -1
                else:
                    self.insert_dude()
                    return True
        self.insert_dude()
        return True
            