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
  new_player = Player(game_name, game_choice)
  player.append(new_player)
  print('HHHH', str(request.form))
  return redirect('/game')


@app.route('/game')
def game():
  import random
  game_list = ['Rock', 'Paper', 'Scissors']
  computer_choice = random.choice(game_list)
  print(computer_choice)

  # [Player{self.name, self.choice}]
  current_player = player[0]

  player_choice = current_player.choice
  print('player choice:', player_choice)
  player_name = current_player.name

  if player_choice == computer_choice:
    return f"Player1 choice:{player_name}: {computer_choice}, Computer choice \nThis is a draw"

  elif player_choice == 'Rock':
    if computer_choice == 'Scissors':
      return f"{player_name} Player1 is the Winner!!"
    else:
      return f"{computer_choice} Computer win is the Winner!!"

  elif player_choice == 'Paper':
    if computer_choice == "Rock":
      return f"{player_name}: Player1 is the Winner!!"
    else:
      return f"{computer_choice} Computer win is the Winner!!"

  elif player_choice == 'Rock':
    if computer_choice == 'Scissors':
      return f"{player_name}:  Player1 is the Winner!!"
    else:
      return f"{computer_choice} Computer winsis the Winner!!"
  else:
    return "Didn't work, Come on you can do it. Don't give up yet!"

