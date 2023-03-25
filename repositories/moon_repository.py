from db.run_sql import run_sql

from models.moon import Moon
import repositories.planet_repository as planet_repository

def save(moon):
    sql = "INSERT INTO moons (name, planet_id, orbital_period, mean_radius) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [moon.name, moon.planet.id, moon.orbital_period, moon.mean_radius]
    results = run_sql(sql, values)
    id = results[0]['id']
    moon.id = id
    return moon

def select_moons(id):
    moons = []
    sql = "SELECT * FROM moons WHERE planet_id = %s"
    values = [id]
    results = run_sql(sql, values)

    for row in results:
        planet = planet_repository.select(row['planet_id'])
        moon = Moon(row['name'], planet, row['orbital_period'], row['mean_radius'], row['id'] )
        moons.append(moon)
    return moons

def select_moon(moon_id, planet_id):
    sql = "SELECT * FROM moons WHERE id = %s"
    values = [moon_id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        planet = planet_repository.select(planet_id)
        moon = Moon(result['name'], planet, result['orbital_period'], result['mean_radius'], result['id'] )
    return moon

def update(moon):
    sql = "UPDATE moons SET (name, planet_id, orbital_period, mean_radius) = (%s, %s, %s, %s) WHERE id = %s"
    values = [moon.name, moon.planet.id, moon.orbital_period, moon.mean_radius, moon.id]
    print(values)
    run_sql(sql, values)


def delete(moon_id):
    sql = "DELETE  FROM moons WHERE id = %s"
    values = [moon_id]
    run_sql(sql, values)

