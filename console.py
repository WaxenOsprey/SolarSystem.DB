import pdb
from models.planet import Planet
from models.moon import Moon
from models.user import User
from models.visit import Visit

import repositories.planet_repository as planet_repository
import repositories.moon_repository as moon_repository
import repositories.user_repository as user_repository
import repositories.visit_repository as visit_repository

# task_repository.delete_all()
# user_repository.delete_all()
# pdb.set_trace()
# moons = moon_repository.select_moons(4)
# planet = planet_repository.select(4)

# for moon in moons:
#     print(f"{moon.name}")

pdb.set_trace()
user = User('paul', True)
user_repository.save_user(user)
planet = Planet('Eros', '345', '45', '3g')
visit_repository.save_visit(user, planet)

# error here visit is empty or something
visit = visit_repository.select_visit(user, planet)
# mark discovered
visit.mark_discovered()
# save to dbn
visit_repository.update_status(visit)
