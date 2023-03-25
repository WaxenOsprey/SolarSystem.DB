DROP TABLE IF EXISTS visits;
DROP TABLE IF EXISTS moons;
DROP TABLE IF EXISTS planets;
DROP TABLE IF EXISTS users;


-- use decimal for decimals numbers

CREATE TABLE planets (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  mass VARCHAR(255),
  temp VARCHAR(255),
  gravity VARCHAR(255)
);

CREATE TABLE moons (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  planet_id INT NOT NULL REFERENCES planets(id) ON DELETE CASCADE,
  orbital_period VARCHAR(255),
  mean_radius VARCHAR(255)
);

CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  active BOOL
);

CREATE TABLE visits (
  id SERIAL PRIMARY KEY,
  user_id INT REFERENCES users(id) ON DELETE CASCADE,
  location_name VARCHAR(255)
);

INSERT INTO planets (name, mass, temp, gravity) VALUES ('Mercury', '0.055 Earths', '-73℃ - 164℃', '0.38g');
INSERT INTO planets (name, mass, temp, gravity) VALUES ('Venus', '0.815 Earths', '464℃', '0.904g');
INSERT INTO planets (name, mass, temp, gravity) VALUES ('Earth', '1.0 Earths', '14℃', '1.0g');
INSERT INTO planets (name, mass, temp, gravity) VALUES ('Mars', '0.107 Earths', '-60℃', '0.37g');
INSERT INTO planets (name, mass, temp, gravity) VALUES ('Jupiter', '317.8 Earths', '-108℃', '2.52g');
INSERT INTO planets (name, mass, temp, gravity) VALUES ('Saturn', '95.15 Earths', '-139℃', '1.065g');
INSERT INTO planets (name, mass, temp, gravity) VALUES ('Neptune', '17.14 Earths', '-201℃', '1.14g');
INSERT INTO planets (name, mass, temp, gravity) VALUES ('Uranus', '14.53 Earths', '-197℃', '0.88g');
INSERT INTO planets (name, mass, temp, gravity) VALUES ('Pluto', '0.055 Earths', '-164℃', '0.38g');

INSERT INTO moons (name, planet_id, orbital_period, mean_radius) VALUES ('The Moon', 3, '27 days', '1737km');
INSERT INTO moons (name, planet_id, orbital_period, mean_radius) VALUES ('Phobos', 4, '0.3 days', '11.2km');
INSERT INTO moons (name, planet_id, orbital_period, mean_radius) VALUES ('Deimos', 4, '1.2 days', '6.2km');


