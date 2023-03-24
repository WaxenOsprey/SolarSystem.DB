from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.planet import Planet
import repositories.planet_repository as planet_repository

planets_blueprint = Blueprint("planets", __name__)

@planets_blueprint.route("/planets")
def planets():
    planets = planet_repository.select_all()
    return render_template("planets/index.html", all_planets = planets)

# SHOW (GETS AN INDIVIDUAL PLANET, and renders the single planet page)
# GET '/planets/<id>'
@planets_blueprint.route("/planets/<id>", methods=['GET'])
def show_planet(id):
    planet = planet_repository.select(id)
    return render_template('planets/show.html', planet = planet) 


# GET '/planets/new' (THIS GOES TO PAGE WITH FOR NEW PLANET)
@planets_blueprint.route("/planets/new", methods=['GET'])
def new_planet():
    return render_template("planets/new.html")

# CREATE (THIS DEALS WITH THE REQUEST SEND BY THE FORM AND CREATES A NEW BOOK)
# POST '/planets'
@planets_blueprint.route("/planets",  methods=['POST']) # number one 
def create_planet(): # number two
    name = request.form['name']  # number two 
    mass = request.form['mass']  # number two
    temp = request.form['temp'] # number two
    gravity = request.form['gravity']
    planet = Planet(name, mass, temp, gravity) # number two
    planet_repository.save(planet) # number three 
    return redirect("/planets") # number four 

# EDIT (GETS EDIT PAGE/FORM)
# GET '/planets/<id>/edit'
@planets_blueprint.route("/planets/<id>/edit", methods=['GET'])
def edit_planet(id):
    planet = planet_repository.select(id)
    return render_template('planets/edit.html', planet = planet)

# UPDATE (POSTS EDIT PAGE CONTENTS, to edit data)
# PUT '/planets/<id>'
@planets_blueprint.route("/planets/<id>", methods=['POST'])
def update_planet(id):
    name = request.form['name']
    mass = request.form['mass']
    temp = request.form['temp']
    gravity = request.form['temp']
    planet = Planet(name, mass, temp, gravity, id)
    planet_repository.update(planet)
    return redirect('/planets')

# # DELETE (AT THIS POINT THIS RELIES A DELETE BUTTON AJOINED TO EACH PLANET, OTHERWISE WE NEED A GET and a DELETE page, then a POST)
# # DELETE '/planets/<id>'
@planets_blueprint.route("/planets/<id>/delete", methods=['POST'])
def delete_planet(id):
    planet_repository.delete(id)
    return redirect('/planets')
