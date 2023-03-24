import pdb
from flask import Flask, render_template, request, redirect
from flask import Blueprint
import repositories.moon_repository as moon_repository
import repositories.planet_repository as planet_repository

moons_blueprint = Blueprint("moons", __name__)

@moons_blueprint.route("/planets/<planet_id>/moons")
def show_moons(planet_id):
    planet = planet_repository.select(planet_id)
    moons = moon_repository.select_moons(planet_id)
    
    return render_template("planets/moons/index.html", local_moons = moons, planet = planet)

@moons_blueprint.route("/planets/<planet_id>/moons/<moon_id>")
def show_the_moon(moon_id, planet_id):
    random = planet_id
    moon = moon_repository.select_moon(moon_id)
    return render_template("planets/moons/show.html", moon = moon)
    
# GET '/planets/new' (THIS GOES TO PAGE WITH FOR NEW PLANET)
@moons_blueprint.route("/planets/<planet_id>/moons/new", methods=["GET"])
def new_moon(planet_id):
    planet_repository.select(planet_id)
    return render_template("planets/moons/new.html")
