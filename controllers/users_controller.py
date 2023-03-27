import pdb
from flask import Flask, render_template, request, redirect, url_for
from flask import Blueprint
from models.user import User
import repositories.user_repository as user_repository
import repositories.visit_repository as visit_repository

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

@users_blueprint.route("/users/<user_id>", methods=['GET'])
def log_in_user(user_id):
    user = user_repository.select_user_by_id(user_id)
    user_repository.make_other_users_inactive(user)
    user_repository.login_user(user)
    return redirect(url_for('planets.planets'))

@users_blueprint.route("/exit", methods=['GET'])
def exit():
    visits = []
    user = user_repository.select_active_user()
    id = user.id
    visits = visit_repository.select_all_visits(id)
    visits_total = len(visits)
    discoveries = []
    alterations = []
    destructions = []
    for visit in visits:
        if visit.discovered == True:
            discoveries.append(visit)
        elif visit.altered == True:
            alterations.append(visit)
        elif visit.destroyed == True:
            destructions.append(visit)
    discovered_total = len(discoveries)
    altered_total = len(alterations)
    destroyed_total = len(destructions)
    

    return render_template('exit.html', user=user, visits=visits, visits_total=visits_total, discoveries=discoveries, discovered_total=discovered_total, alterations=alterations, altered_total=altered_total, destructions=destructions, destroyed_total=destroyed_total)