import pdb
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.planet import Planet
from models.visit import Visit
import repositories.planet_repository as planet_repository
import repositories.visit_repository as visit_repository
import repositories.user_repository as user_repository
import repositories.moon_repository as moon_repository

planets_blueprint = Blueprint("planets", __name__)

@planets_blueprint.route("/planets")
def planets():
    planets = planet_repository.select_all()
    moons = moon_repository.select_all_moons()
    user = user_repository.select_active_user()
    return render_template("planets/index.html", all_planets = planets, all_moons = moons, user = user)


@planets_blueprint.route("/planets/<id>", methods=['GET'])
def show_planet(id):
    planet = planet_repository.select(id)
    user = user_repository.select_active_user()
    moons = moon_repository.select_moons(id)
    visit_repository.save_visit(user, planet)
    user = user_repository.select_active_user()
    return render_template('planets/show.html', planet = planet, moons = moons, user = user) 


@planets_blueprint.route("/planets/new", methods=['GET'])
def new_planet():
    return render_template("planets/new.html")


@planets_blueprint.route("/planets",  methods=['POST']) 
def create_planet(): 
    name = request.form['name']   
    mass = request.form['mass']  
    temp = request.form['temp'] 
    gravity = request.form['gravity']
    image = request.form['image']
    description = request.form['description']
    planet = Planet(name, mass, temp, gravity, image, description) 
    planet_repository.save(planet)
    
    user = user_repository.select_active_user()
    visit_repository.save_visit(user, planet)
    visit = visit_repository.select_visit(user, planet)
    visit.mark_discovered()
    visit_repository.update_visit(visit)

    return redirect("/planets")


@planets_blueprint.route("/planets/<id>/edit", methods=['GET'])
def edit_planet(id):
    planet = planet_repository.select(id)
    return render_template('planets/edit.html', planet = planet)


@planets_blueprint.route("/planets/<id>", methods=['POST'])
def update_planet(id):
    name = request.form['name']
    mass = request.form['mass']
    temp = request.form['temp']
    gravity = request.form['gravity']
    image = request.form['image']
    description = request.form['description']
    new_planet = Planet(name, mass, temp, gravity, image, description)

    user = user_repository.select_active_user()
    planet_to_update = planet_repository.select(id)
    visit_to_update = visit_repository.select_visit(user, planet_to_update)
    visit_to_update.mark_altered()
    visit_to_update.location = new_planet.name
    visit_repository.update_visit(visit_to_update)
    planet_repository.update(new_planet)

    return redirect('/planets')


@planets_blueprint.route("/planets/<id>/delete", methods=['POST'])
def delete_planet(id):
    planet = planet_repository.select(id)
    user = user_repository.select_active_user()
    visit = visit_repository.select_visit(user, planet)
    visit.mark_destroyed()
    visit_repository.update_visit(visit)
    planet_repository.delete(id)

    return redirect('/planets')


