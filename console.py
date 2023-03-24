import pdb
from models.planet import Planet
from models.moon import Moon

import repositories.planet_repository as planet_repository
import repositories.moon_repository as moon_repository

# task_repository.delete_all()
# user_repository.delete_all()
# pdb.set_trace()
# moons = moon_repository.select_moons(4)
# planet = planet_repository.select(4)

# for moon in moons:
#     print(f"{moon.name}")

moon = moon_repository.select_moon(1)
print(f"{moon.name}")