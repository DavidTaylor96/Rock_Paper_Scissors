from flask import render_template, request, redirect
from app import app
from app.models.game import *
from app.models.player import *

@app.route('/')
def index():
  return render_template('index.html', title='Home', games=player)

@app.route('/', methods=["POST"])
def add_player1():
  game_choice = request.form["choice"]
  game_name = request.form["name"]
  new_player = Player(game_choice, game_name)
  player.append(new_player)
  print('HHHH', str(request.form))
  return redirect('/')


@app.route('/game')
def game():
  import random
  game_list = ['Rock', 'Paper', 'Scissors']
  computer_choice = random.choice(game_list)
  if player.choice == computer_choice:
    return f"Player1 choice:{player.choice}: {computer_choice}, Computer choice \nThis is a draw"

  elif player.choice == 'Rock':
    if computer_choice == 'Scissors':
      return f"{player.name} Player1 is the Winner!!"
    else:
      return f"{computer_choice} Computer win is the Winner!!"

  elif player.choice == 'Paper':
    if computer_choice == "Rock":
      return f"{player.name}: Player1 is the Winner!!"
    else:
      return f"{computer_choice} Computer win is the Winner!!"

  elif player.choice == 'Rock':
    if computer_choice == 'Scissors':
      return f"{player.name}:  Player1 is the Winner!!"
    else:
      return f"{computer_choice} Computer winsis the Winner!!"
  else:
    return "Didn't work, Come on you can do it. Don't give up yet!"

