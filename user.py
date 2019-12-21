import os
def Printer(game,mat,height,width):
    text = ""
    text += "Row: {} Col:{}".format(game.rebels[0].y,game.rebels[0].x)
    for row in range(height):
        text += "\n"
        for col in range(width):
            text += mat[row][col].t
    os.system('clear')
    print (text)