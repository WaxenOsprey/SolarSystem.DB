from db.run_sql import run_sql

from models.user import User

def save_user(user):
    sql = "INSERT INTO users( name, active ) VALUES ( %s, %s ) RETURNING id"
    values = [user.name, user.active]
    results = run_sql( sql, values )
    user.id = results[0]['id']
    return user

def make_other_users_inactive(user):
    id = user.id
    sql = "UPDATE users SET active = False WHERE id != %s"
    values = [id]
    run_sql( sql, values )

def select_active_user():
    sql = "SELECT * FROM users WHERE active = %s"
    values = [True]
    results = run_sql( sql, values )
    if results:
        result = results[0]
        user = User(result['name'], result['active'], result['id'])
    return user

def select_all_users():
    users = []
    sql = "SELECT * FROM users"
    results = run_sql(sql)

    for row in results:
        user = User(row['name'], row['active'], row['id'])
        users.append(user)
    return users

def select_user_by_id(user_id):
    sql = "SELECT * FROM users WHERE id = %s"
    values = [user_id]
    results = run_sql( sql, values)
    if results:
        result = results[0]
        user = User(result['name'], result['active'], result['id'])
    return user

def login_user(user):
    user.active = True
    sql = "UPDATE users SET (name, active) = (%s, %s) WHERE id = %s"
    values = [user.name, user.active, user.id]
    run_sql(sql, values)
