def player_info(rebel):
    string = 'b'        #indicating which character will be shown 0
    id = rebel.id
    string += str(id) + "0"    #player ID indicating other stuff about the character 1-2   (1,3)
    string += '000000'    #3-8
    y = str(rebel.y)                        
    string += str(int(4-len(y)) * '0') + y  #4 digit number, the Y axis of the player  9-12 (9,13)
    #print (str(int(4-len(y))))
    #print (str(int(4-len(y)) * '0'))
    x = str(rebel.x)
    string += str( int(4-len(x)) * '0') + x  #4 digit number, the X axis of the player 13-16 (13,17)(might change this to larger number if the map gets longer)
    width  = str(rebel.width)
    height = str(rebel.height)
    health = str(rebel.health)
    string += str(int(4-len(width)) * '0') + width      #17-20  (17,21)
    string += str(int(4-len(height)) * '0') + height    #21-24  (21,25)
    string += str(int(4-len(health)) * '0') + health    #4 digit number with the health of the player  25-28 (25-29)
    #print (len(string))
    return string
def Send_To_Client(game):
    string = ""
    string += str(game.players) + "<br>" #0  <br> 1-4 
    for i in range(game.players):
        string += player_info(game.rebels[i]) + '<br>' #21-24
    return string
