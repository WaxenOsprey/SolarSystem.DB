import pdb
from flask import Flask, render_template, request, redirect, url_for
from flask import Blueprint
from models.user import User
import repositories.user_repository as user_repository

users_blueprint = Blueprint("users", __name__)

@users_blueprint.route("/")
def log_in_page():
    users = user_repository.select_all_users()
    return render_template('index.html', users = users)


@users_blueprint.route("/", methods=['POST'])
def create_user():
    name = request.form['name']
    active = True
    user = User(name, active)
    user_repository.save_user(user)
    user_repository.make_other_users_inactive(user)
    return redirect(url_for('planets.planets'))

# @users_blueprint.route("/login", methods=['POST'])
# def login_user():
#     name = request.form['name']

users_blueprint.route("/exit", method=['GET'])
def exit():
    return render_template("exit.html")