from flask import Blueprint, render_template
from . import db
from flask_login import login_required , current_user

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/gameboard')
@login_required
def gameboard():
    return render_template('gameBoard.html',name = current_user.name)

@main.route('/gameplay')
@login_required
def gameplay():
    return render_template('gamePlay.html',name = current_user.name)