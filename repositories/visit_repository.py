from db.run_sql import run_sql
from models.visit import Visit

def save_visit(user, location):
    sql = "INSERT INTO visits ( user_id, location_name) VALUES ( %s, %s )"
    values = [user.id, location.name]
    run_sql( sql, values )
    return

def select_visit(user, location):
    # not completely sure about this sql command
    sql = "SELECT * FROM visits WHERE user_id = %s AND location_name = %s"
    values = [user.id, location.name]
    results = run_sql( sql, values )
        # checking if the list returned by `run_sql(sql, values)` is empty. Empty lists are false.
    if results:
        result = results[0]
        # like in previous functions might need to just attach a user here
        selected_visit = Visit(result['user_id'], result['location_name'], result['discovered'], result['altered'], result['destroyed'], result['id'] )
    return selected_visit

def update_visit(visit):    
    sql = "UPDATE visits SET (user_id, location_name, discovered, altered, destroyed) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [visit.user, visit.location, visit.discovered, visit.altered, visit.destroyed, visit.id]
    run_sql (sql, values) 

def select_all_visits(id):
    visits = []
    sql = "SELECT * FROM visits WHERE user_id = %s"
    values = [id]
    results = run_sql(sql, values)

    for row in results:
        visit = Visit(row['user_id'], row['location_name'], row['discovered'], row['altered'], row['destroyed'])
        visits.append(visit)
    return visits