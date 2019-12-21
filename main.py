
import os 
from game import game 
import time 
import threading
from flask_cors import CORS

from flask import Flask, escape, request

app = Flask(__name__)
CORS(app)
def press(d):
    return d

game = game(50,100,2)

d = []
def testrun(game):
    string = ""
    string += str(game.players)
    for i in range(game.players):
        string += player_info(game.rebels[i])
    return string
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

game.round()
def round():
    time.sleep(3)
    while True:
        time.sleep(0.1)
        game.round()

r = threading.Thread(target=(round))
r.start()

#sends info about moving targets to /loc
@app.route('/loc')
def hello():
    print ("Sent info")
    return testrun(game)

@app.route('/update/<player>/<keys>')
def keylogger(player,keys):
    print ("for Player: {} got keys: {}".format(player,keys))
    for key in keys:
        game.rebels[int(player)].keys_pressed.append(key)
    return str(game.rebels[int(player)].keys_pressed)
if __name__ == '__main__':
    app.run()
