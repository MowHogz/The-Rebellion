# The-Rebellion
The Server-Side (Backend) to "The Rebles" game in the Hackathon
FLASK_APP=main.py flask run --host=0.0.0.0

For Beta Updates (in the browser):
http://localhost:5000/update

To control players: 
http://localhost:5000/update/<No. Player (counting from 0)>/ (controls, For now WASD - works with more than 1 at a time)

To get visual updates (For GUI on Front-End):
http://localhost:5000/loc
number of players

(The coming up info repeats itself based on number of players)

Character info (for now there is only 0)
'Posture' 0    - right 1 - left
'position'     - jump,fireball,kama,blonde,punch,stand,left punch (didn't number them yet)
y              - (location of player on the Y Axis)
x              - (location of player on the X Axis) 
health         - (number) (health of current player)




number of balls (Other elements on screen)
0 - position/look (No. of moving element (what picture to show))
y (location)
x (location)
