
import os 

from flask import render_template
from game import game 
import time 
import threading
from flask_cors import CORS
from output import player_info,Send_To_Client as game_info

from flask import Flask, escape, request

app = Flask(__name__, template_folder="HTML", static_folder="static")

CORS(app)
def press(d):
    return d


game = game(800,1000,2)

d = []
def output(game,mat,height,width):#outputs the 'beta testing' version of the game into the webpage (requires refreshing)
    text = ""
    text += "Row: {} Col:{}".format(game.rebels[0].y,game.rebels[0].x)
    for row in range(height):
        text += "<br>"
        for col in range(width):
            text += mat[row][col].t
    return (text)

game.round()
def round(): #Another Frame 
    time.sleep(3)
    while True:
        time.sleep(0.1)
        if game.sleep:
            game.sleep = False
            time.sleep(3)
        game.round()
        print (game_info(game))

r = threading.Thread(target=(round))
r.start()
@app.route('/')
def home():
    return "You Have reached the home page of the website"

@app.route('/reset')
def reset():
    game = game(800,1000,2)
    return "Succesfully reset "


@app.route('/play')
def play():
    return render_template("play.html")
    
    return "Hello World"


@app.route('/update')
def update():
    return output(game,game.map,game.height,game.width)
#sends info about moving targets to /loc
@app.route('/loc')
def hello():
    #print ("Sent info")
    return game_info(game)
@app.route('/input/<player>/<keys>')

def keylogger(player,keys):
    
    print ("for Player: {} got keys: {}".format(player,keys))
    time.sleep(2)
    for key in keys:
        game.rebels[int(player)].keys_pressed.append(key)
    return str(game.rebels[int(player)].keys_pressed)
if __name__ == '__main__':
    app.run(debug = True)
