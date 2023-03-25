import pdb
from flask import Flask, render_template, request, redirect, url_for
from flask import Blueprint
from models.moon import Moon
from models.planet import Planet
import repositories.moon_repository as moon_repository
import repositories.planet_repository as planet_repository
import repositories.user_repository as user_repository
import repositories.visit_repository as visit_repository


moons_blueprint = Blueprint("moons", __name__)

@moons_blueprint.route("/planets/<planet_id>/moons")
def show_moons(planet_id):
    planet = planet_repository.select(planet_id)
    moons = moon_repository.select_moons(planet_id)
    
    return render_template("planets/moons/index.html", local_moons = moons, planet = planet)

@moons_blueprint.route("/planets/<planet_id>/moons/<moon_id>")
def show_the_moon(planet_id, moon_id):
    moon = moon_repository.select_moon(moon_id, planet_id)
    planet = planet_repository.select(planet_id)
    user = user_repository.select_active_user()
    visit_repository.save_visit(user, moon)
    return render_template("planets/moons/show.html", moon = moon, planet = planet)
    
# GET '/planets/new' (THIS GOES TO PAGE WITH FOR NEW MOON)
@moons_blueprint.route("/planets/<planet_id>/moons/new", methods=["GET"])
def new_moon(planet_id):
    planet_repository.select(planet_id)
    return render_template("planets/moons/new.html", planet_id = planet_id)

@moons_blueprint.route("/planets/<planet_id>/moons/new",  methods=['POST']) # number one 
def create_moon(planet_id): # number two
    name = request.form['name']  # number two 
    orbital_period = request.form['orbital_period'] 
    mean_radius = request.form['mean_radius'] 
    #need planet object, cant just use planet_id
    selected_planet = planet_repository.select(planet_id)
    moon = Moon(name, selected_planet, orbital_period, mean_radius)
    moon_repository.save(moon)
    # needs better url 
    return redirect(url_for('planets.planets'))

# GO TO EDIT PAGE
@moons_blueprint.route("/planets/<planet_id>/moons/<moon_id>/edit", methods=['GET'])
def edit_moon(moon_id, planet_id):
    # possibly reduntant code 
    selected_moon = moon_repository.select_moon(moon_id, planet_id)
    selected_planet = planet_repository.select(planet_id)
    return render_template("planets/moons/edit.html", moon = selected_moon, planet = selected_planet)

# POST FROM EDIT PAGE
@moons_blueprint.route("/planets/<planet_id>/moons/<moon_id>/edit", methods=['POST'])
def update_moon(planet_id, moon_id):
    pdb.set_trace
    name = request.form['name']
    orbital_period = request.form['orbital_period']
    mean_radius = request.form['mean_radius']
    planet = planet_repository.select(planet_id)
    moon = Moon(name, planet, orbital_period, mean_radius, moon_id)
    moon_repository.update(moon)
    # needs better url
    return redirect(url_for('planets.planets'))


@moons_blueprint.route("/planets/<planet_id>/moons/<moon_id>/delete", methods=['POST'])
def delete_moon(moon_id, planet_id):
    moon_repository.delete(moon_id)
    # needs better url
    return redirect(url_for('planets.planets'))
