
import os 
from game import game 
import time 
import threading
from flask_cors import CORS
from output import player_info,Send_To_Client as game_info

from flask import Flask, escape, request

app = Flask(__name__)
CORS(app)
def press(d):
    return d

game = game(50,100,2)

d = []
def output(game,mat,height,width):
    text = ""
    text += "Row: {} Col:{}".format(game.rebels[0].y,game.rebels[0].x)
    for row in range(height):
        text += "<br>"
        for col in range(width):
            text += mat[row][col].t
    return (text)

game.round()
def round():
    time.sleep(3)
    while True:
        time.sleep(0.1)
        game.round()

r = threading.Thread(target=(round))
r.start()
@app.route('/update')
def update():
    return output(game,game.map,game.height,game.width)
#sends info about moving targets to /loc
@app.route('/loc')
def hello():
    print ("Sent info")
    return game_info(game)

@app.route('/input/<player>/<keys>')
def keylogger(player,keys):
    print ("for Player: {} got keys: {}".format(player,keys))
    for key in keys:
        game.rebels[int(player)].keys_pressed.append(key)
    return str(game.rebels[int(player)].keys_pressed)
if __name__ == '__main__':
    app.run()
