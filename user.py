from output import Send_To_Client
import os
def Printer(game,mat,height,width):
    text = ""
    text += "Row: {} Col:{}".format(game.rebels[0].y,game.rebels[0].x)
    for row in range(height):
        text += "\n"
        for col in range(width):
            text += mat[row][col].t
    text += Send_To_Client(game)
    os.system('clear')
    print (text)