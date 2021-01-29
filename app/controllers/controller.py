from flask import render_template, request, redirect
from app import app
from app.models.game import *
from app.models.player import *

@app.route('/')
def index():
  return render_template('index.html', title='Home', games=player)

@app.route('/game')
def game():
  if game.choice == game.choice:
    return "draw"

  elif game.choice == 'Rock':
    if game.choice == 'Scissors':
      return f"{game.name}: Player1 is the Winner!!"
    else:
      return f"{game.name}: Player2 is the Winner!!"

  elif game.choice == "Paper":
    if game.choice == "Rock":
      return f"{game.name}: Player1 is the Winner!!"
    else:
      return f"{game.name}: Player2 is the Winner!!"

  elif game.choice == 'Rock':
    if game.choice == 'Scissors':
      return f"{game.name}:  Player1 is the Winner!!"
    else:
      return f" {game.name}: Player2 is the Winner!!"
  else:
    return "Wrong Command!"


@app.route('/', methods=["POST"])
def add_player():
  game_name = request.form["name"]
  game_choice = request.form["choice"]
  new_player = Player(game_name, game_choice)

  player.append(new_player)
  return redirect('/')