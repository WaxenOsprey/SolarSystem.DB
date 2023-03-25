from db.run_sql import run_sql

from models.user import User

def save_user(user):
    # problems might arise below because of True not being recognised as 1 in sql
    sql = "INSERT INTO users( name, active ) VALUES ( %s, %s ) RETURNING id"
    values = [user.name, user.active]
    results = run_sql( sql, values )
    # I dont understand why this is happening below?
    user.id = results[0]['id']
    return user

def select_active_user():
    sql = "SELECT * FROM users WHERE active = %s"
    values = [True]
    results = run_sql( sql, values )
    if results:
        result = results[0]
        user = User(result['name'], result['active'], result['id'])
    return user