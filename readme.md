
# SolarSystem.DB 🚀✨🪐

## Overview

SolarSystem.DB was built as a solo project during the 5th week of the CodeClan Professional Software Development course. Built with Python, Flask, PostgreSQL, HTML and CSS, the application allows users to explore and catalogue the Solar System. Implementing full CRUD functionality, users can create, read, update and delete planets and moons. The app also allows users to travel from the sun to each planet/moon and view information about the planet. The app also allows users to see a summary of their activities at the end of their visit.

## Project Setup

### Install Homebrew

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```

### Clone the repo

```
git clone https://github.com/WaxenOsprey/SolarSystem.DB.git
```

### Install PostgreSQL

```
brew install postgresql
```

### Install Python3

```
brew install python3
```

### Install Flask

```
pip3 install flask
```

### Install psycopg2

```
pip3 install psycopg2
```


### Create the database

```
createdb solar_system
```

### Run the web app

```
flask run
```

## Project Specification

Choose a domain or app that you have an interest in and design & build a full stack Flask app.

The project must be built using only:
* HTML / CSS
* Python
* Flask
* PostgreSQL and the psycopg

It must **NOT** use:
* Any Object Relational Mapper (e.g. ActiveRecord)
* JavaScript. At all. Don't even think about it.
* Any pre-built CSS libraries, such as Bootstrap.
* Authentication. Assume that the user already has secure access to the app.

Timeframe: 1 week


## Project Brief

Build an app that allows a user to explore and catalogue the solar system.

### MVP

- The app should allow the user to create (discover) new moons and planets and edit their properties
- The app should allow the user to travel from the sun to each planet/moon and view information about the planet
- The app should allow the user to destroy any solar system object.

### Possible Extensions

- The app should allow the user to see a summary of their activities at the end of their visit
- Show distance to sun at each solar system object
- The app could have the capabilities to discover, edit, and destroy other objects in solar system e.g. asteroids/comets.






