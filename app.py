from flask import Flask, render_template

from controllers.planets_controller import planets_blueprint
from controllers.moons_controller import moons_blueprint
from controllers.users_controller import users_blueprint

app = Flask(__name__)

app.register_blueprint(planets_blueprint)
app.register_blueprint(moons_blueprint)
app.register_blueprint(users_blueprint)


if __name__ == '__main__':
    app.run(debug=True)
