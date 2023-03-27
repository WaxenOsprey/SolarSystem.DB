import pdb
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.planet import Planet
from models.visit import Visit
import repositories.planet_repository as planet_repository
import repositories.visit_repository as visit_repository
import repositories.user_repository as user_repository

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
    user = user_repository.select_active_user()
    visit_repository.save_visit(user, planet)
    return render_template('planets/show.html', planet = planet) 


# GET '/planets/new' (THIS GOES TO PAGE WITH FOR NEW PLANET)
@planets_blueprint.route("/planets/new", methods=['GET'])
def new_planet():
    return render_template("planets/new.html")

# CREATE (THIS DEALS WITH THE REQUEST SENT BY THE FORM AND CREATES A NEW BOOK)
# POST '/planets'
@planets_blueprint.route("/planets",  methods=['POST']) # number one 
def create_planet(): 
    # takes new planet data from form and saves values to vars
    name = request.form['name']   
    mass = request.form['mass']  
    temp = request.form['temp'] 
    gravity = request.form['gravity']
    image = request.form['image']
    # create new planet object with values from vars
    planet = Planet(name, mass, temp, gravity, image) 
    # saves to db
    planet_repository.save(planet)
    
    user = user_repository.select_active_user()
    visit_repository.save_visit(user, planet)
    visit = visit_repository.select_visit(user, planet)
    visit.mark_discovered()
    visit_repository.update_visit(visit)


    return redirect("/planets")

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
    gravity = request.form['gravity']
    image = request.form['image']
    new_planet = Planet(name, mass, temp, gravity, image, id)

    user = user_repository.select_active_user()
    planet_to_update = planet_repository.select(id)
    visit_to_update = visit_repository.select_visit(user, planet_to_update)
    visit_to_update.mark_altered()
    visit_to_update.location = new_planet.name
    visit_repository.update_visit(visit_to_update)
    planet_repository.update(new_planet)


    return redirect('/planets')

# # DELETE (AT THIS POINT THIS RELIES A DELETE BUTTON AJOINED TO EACH PLANET, OTHERWISE WE NEED to put it in show planet)
# # DELETE '/planets/<id>'
@planets_blueprint.route("/planets/<id>/delete", methods=['POST'])
def delete_planet(id):
    planet = planet_repository.select(id)
    user = user_repository.select_active_user()
    visit = visit_repository.select_visit(user, planet)
    visit.mark_destroyed()
    visit_repository.update_visit(visit)
    planet_repository.delete(id)

    return redirect('/planets')


