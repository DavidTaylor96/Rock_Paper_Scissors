from flask import render_template, request, redirect
from app import app
from app.models.game import *
from app.models.player import *

@app.route('/')
def index():
  return render_template('index.html', title='Home', game1=player_1, game2=player_2)

@app.route('/', methods=["POST"])
def add_player1():
  game1_name = request.form["name1"]
  game1_choice = request.form["choice1"]
  new_player = Player1(game1_name, game1_choice)

  player_1.append(new_player)
  print('HHHH', str(player_1))
  return redirect('/')

@app.route('/', methods=["POST"])
def add_player2():
  game2_name = request.form["name2"]
  game2_choice = request.form["choice2"]
  new_player = Player2(game2_name, game2_choice)

  player_2.append(new_player)
  print('LLLLL', str(player_2))
  return redirect('/')


@app.route('/game')
def game():
  if player1.choice == player2.choice:
    return f"Player1 choice:{player1.choice}\n,Player2 choice: {player2.choice},\n,This is a draw"

  elif player1.choice == 'Rock':
    if player2.choice == 'Scissors':
      return f"{player1.name}: Player1 is the Winner!!"
    else:
      return f"{player2.name}: Player2 is the Winner!!"

  elif player1.choice == "Paper":
    if player2.choice == "Rock":
      return f"{player1.name}: Player1 is the Winner!!"
    else:
      return f"{player2.name}: Player2 is the Winner!!"

  elif player1.choice == 'Rock':
    if player2.choice == 'Scissors':
      return f"{player1.name}:  Player1 is the Winner!!"
    else:
      return f" {player2.name}: Player2 is the Winner!!"
  else:
    return "Wrong Command!"

