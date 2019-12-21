from space import space 
class bullet():
    def __init__(self,game,y,x,pace,height,width):
        self.game = game
        self.y = y
        self.x = x
        self.pace = pace
        self.height = height 
        self.width = width 
        self.nezeq = 4
        self.active = True
        if pace > 0:
            self.right = True
        else: 
            self.right = False
    def move(self):
        if self.pace > 0:
            for i in range(self.pace):
                self.x += 1
                if self.hit_anything_in_way():
                    return True
        else:
            for i in range(abs(self.pace)):
                self.x += -1
                if self.hit_anything_in_way():
                    return True
        return False
    def hit_anything_in_way(self):
        if self.game.map[self.y][self.x].get_hit(self.nezeq,self.pace):
            self.active = False
            return True
        return False
        

