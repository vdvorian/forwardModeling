from HS import *
from wood import *

bulk = [0.04]
prop = [100]
dens = [0.0012]

print(get_bulk_modulus_by_wood(bulk, prop))
print(get_velocity_by_wood(get_bulk_modulus_by_wood, bulk, dens, prop))


