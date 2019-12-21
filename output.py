def player_info(rebel):
    string = 'b'
    string += '0000'
    string += '0000'
    y = str(rebel.y)
    string += str(int(4-len(y)) * '0') + y
    x = str(rebel.x)
    string += str(int(4-len(y)) * '0') + y
    health = str(rebel.health)
    string += str(int(4-len(health)) * '0') + health
    return string
def Send_To_Client(game):
    string = ""
    string += str(game.players)
    for i in range(game.players):
        string += player_info(game.rebels[i])
    return string
