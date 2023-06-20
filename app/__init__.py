from flask import Flask, render_template
import generator

app = Flask(__name__)

@app.route('/')
def home():
    game_map = generator.gameMap(15, 10, 30)
    return render_template('index.html', game_map=game_map)

