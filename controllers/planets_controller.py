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
# @planets_blueprint.route("/planets/new", methods=['GET'])
# def new_book():
#     authors = author_repository.select_all()
#     return render_template("books/new.html", all_authors = authors)

# CREATE (THIS DEALS WITH THE REQUEST SEND BY THE FORM AND CREATES A NEW BOOK)
# POST '/books'
# @books_blueprint.route("/books",  methods=['POST']) # number one 
# def create_book(): # number two
#     title    = request.form['title']  # number two 
#     genre = request.form['genre']  # number two
#     publisher   = request.form['publisher'] # number two
#     author  = author_repository.select(request.form['author_id']) # number three 
#     book = Book(title, genre, publisher, author) # number two
#     book_repository.save(book) # number three 
    # return redirect("/books/") # number four 

# EDIT
# GET '/books/<id>/edit'
# @books_blueprint.route("/books/<id>/edit", methods=['GET'])
# def edit_book(id):
#     book = book_repository.select(id)
#     authors = author_repository.select_all()
#     return render_template('books/edit.html', book = book, all_authors = authors)

# # UPDATE
# # PUT '/books/<id>'
# @books_blueprint.route("/books/<id>", methods=['POST'])
# def update_book(id):
#     title    = request.form['title']
#     genre = request.form['genre']
#     publisher   = request.form['publisher']
#     author  = author_repository.select(request.form['author_id'])
#     book = Book(title, genre, publisher, author, id)
#     print(book.author.full_name())
#     book_repository.update(book)
#     return redirect('/books')

# # DELETE
# # DELETE '/books/<id>'
# @books_blueprint.route("/books/<id>/delete", methods=['POST'])
# def delete_book(id):
#     book_repository.delete(id)
#     return redirect('/books')
