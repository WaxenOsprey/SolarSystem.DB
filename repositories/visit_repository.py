from db.run_sql import run_sql


def save_visit(user, location):
    sql = "INSERT INTO visits ( user_id, location_name) VALUES ( %s, %s )"
    values = [user.id, location.name]
    run_sql( sql, values )
    return