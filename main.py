from HS import *

bulk = [71, 81]
shear = [30, 49]
prop = 100

print(get_HS_bulk_bounds(bulk, shear, prop))
print(get_HS_shear_bounds(bulk, shear, prop))
print()

bulk_for_many = [71, 81, 63, 45]
shear_for_many = [30, 49, 25, 27]
prop_for_many = [10, 10, 20, 60]

final_bulk, final_shear = get_HS_for_many_components(bulk_for_many, shear_for_many, prop_for_many)
print()
print(final_bulk)
print(final_shear)

print()
print(get_HS_for_many_components(bulk, shear, prop))


prop, bulk_u, bulk_d, shear_u, shear_d = get_HS_for_all_proportions([71, 81], [30, 49], 0.05)
print(len(bulk_u))