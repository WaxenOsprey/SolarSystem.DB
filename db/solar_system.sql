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
  gravity VARCHAR(255),
  image VARCHAR(255)
);

CREATE TABLE moons (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  planet_id INT NOT NULL REFERENCES planets(id) ON DELETE CASCADE,
  orbital_period VARCHAR(255),
  mean_radius VARCHAR(255),
  image VARCHAR(255)
);

CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  active BOOL
);

CREATE TABLE visits (
  id SERIAL PRIMARY KEY,
  user_id INT REFERENCES users(id) ON DELETE CASCADE,
  location_name VARCHAR(255),
  discovered BOOL DEFAULT false,
  altered BOOL DEFAULT false, 
  destroyed BOOL DEFAULT false
);

INSERT INTO planets (name, mass, temp, gravity, image) VALUES ('Mercury', '0.055', 'n/a', '0.38', 'https://upload.wikimedia.org/wikipedia/commons/4/4a/Mercury_in_true_color.jpg');
INSERT INTO planets (name, mass, temp, gravity, image) VALUES ('Venus', '0.815', '464', '0.9', 'http://images2.wikia.nocookie.net/__cb20100109164214/space/images/c/c6/Venus.jpg');
INSERT INTO planets (name, mass, temp, gravity, image) VALUES ('Earth', '1.0', '14', '1.0', 'https://upload.wikimedia.org/wikipedia/commons/c/cb/The_Blue_Marble_%28remastered%29.jpg');
INSERT INTO planets (name, mass, temp, gravity, image) VALUES ('Mars', '0.107', '-60', '0.37', 'https://upload.wikimedia.org/wikipedia/commons/0/0e/Tharsis_and_Valles_Marineris_-_Mars_Orbiter_Mission_%2830055660701%29.png');
INSERT INTO planets (name, mass, temp, gravity, image) VALUES ('Jupiter', '317.8', '-108', '2.52', 'https://upload.wikimedia.org/wikipedia/commons/c/c1/Jupiter_New_Horizons.jpg');
INSERT INTO planets (name, mass, temp, gravity, image) VALUES ('Saturn', '95.15', '-139', '1.06', 'https://images.unsplash.com/photo-1614732414444-096e5f1122d5?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2574&q=80');
INSERT INTO planets (name, mass, temp, gravity, image) VALUES ('Neptune', '17.14', '-201', '1.14', 'https://upload.wikimedia.org/wikipedia/commons/c/c9/Uranus_as_seen_by_NASA%27s_Voyager_2_%28remastered%29_-_JPEG_converted.jpg');
INSERT INTO planets (name, mass, temp, gravity, image) VALUES ('Uranus', '14.53', '-197', '0.88', 'https://upload.wikimedia.org/wikipedia/commons/6/63/Neptune_-_Voyager_2_%2829347980845%29_flatten_crop.jpg');
INSERT INTO planets (name, mass, temp, gravity, image) VALUES ('Pluto', '0.055', '-164', '0.38', 'https://upload.wikimedia.org/wikipedia/commons/e/ef/Pluto_in_True_Color_-_High-Res.jpg');

INSERT INTO moons (name, planet_id, orbital_period, mean_radius, image) VALUES ('The Moon', 3, '27', '1737', 'https://upload.wikimedia.org/wikipedia/commons/e/e1/FullMoon2010.jpg');
INSERT INTO moons (name, planet_id, orbital_period, mean_radius, image) VALUES ('Phobos', 4, '0.3', '11.2', 'https://upload.wikimedia.org/wikipedia/commons/5/5c/Phobos_colour_2008.jpg');
INSERT INTO moons (name, planet_id, orbital_period, mean_radius, image) VALUES ('Deimos', 4, '1.2', '6.2', 'https://upload.wikimedia.org/wikipedia/commons/8/86/NASA-Deimos-MarsMoon-20090221.jpg');
INSERT INTO moons (name, planet_id, orbital_period, mean_radius, image) VALUES ('Io', 5, '1.7', '1821', 'https://upload.wikimedia.org/wikipedia/commons/7/7b/Io_highest_resolution_true_color.jpg');
INSERT INTO moons (name, planet_id, orbital_period, mean_radius, image) VALUES ('Europa', 5, '3.5', '1560', 'https://upload.wikimedia.org/wikipedia/commons/e/e4/Europa-moon-with-margins.jpg');
INSERT INTO moons (name, planet_id, orbital_period, mean_radius, image) VALUES ('Ganymede', 5, '7.1', '2634', 'https://upload.wikimedia.org/wikipedia/commons/2/21/Ganymede_-_Perijove_34_Composite.png');
INSERT INTO moons (name, planet_id, orbital_period, mean_radius, image) VALUES ('Calisto', 5, '16', '2410', 'https://upload.wikimedia.org/wikipedia/commons/2/2f/Callisto_-_July_8_1979_%2838926064465%29.jpg');

