from db.run_sql import run_sql

from models.planet import Planet
import repositories.planet_repository as planet_repository


def save(planet):
    sql = "INSERT INTO planets (name, mass, temp, gravity, image, description) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"
    values = [planet.name, planet.mass, planet.temp, planet.gravity, planet.image, planet.description]
    results = run_sql(sql, values)
    id = results[0]['id']
    planet.id = id
    return planet


def select_all():
    planets = []

    sql = "SELECT * FROM planets"
    results = run_sql(sql)

    for row in results:
        planet = Planet(row['name'], row['mass'], row['temp'], row['gravity'], row['image'], row['description'], row['id'])
        planets.append(planet)
    return planets



def select(id):
    planet = None
    sql = "SELECT * FROM planets WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        planet = Planet(result['name'], result['mass'], result['temp'], result['gravity'], result['image'], result['description'], result['id'] )
    return planet

def delete(id):
    sql = "DELETE  FROM planets WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(planet):
    sql = "UPDATE planets SET (name, mass, temp, gravity, image, description) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [planet.name, planet.mass, planet.temp, planet.gravity, planet.image, planet.description, planet.id]
    print(values)
    run_sql(sql, values)
