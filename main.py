from HS import *
from SCA import *
from DEM import *
from wood_gassmann import *
from forward_problem import *

import matplotlib.pyplot as plt
from time import time
from math import *


calcite = [70.8, 30.3]
dolomite = [80.2, 48.8]
anhydrite = [59.1, 31.4]
illite = [25.3, 16.3]

gas = [0.041, 0]
water = [2.496, 0]

props = [40, 30, 15, 10, 5]
rho_components = [2.71, 2.87, 2.97, 2.52, 1]


vp, vs, time = do_forward_problem(get_proportion_for_HS, get_moduli_by_HS, get_moduli_by_SCA, get_moduli_by_DEM,
                       get_fluid_modulus_by_wood, get_saturated_by_gassman, get_velocity,
                       calcite, dolomite, anhydrite, illite, water, gas, props, rho_components)

print(vp, vs)
print(time)


cal_dol_anh_ill, fluid = do_forward_problem_matrix(get_proportion_for_HS, get_moduli_by_HS, get_moduli_by_SCA, get_moduli_by_DEM,
                       get_fluid_modulus_by_wood, get_saturated_by_gassman, get_velocity,
                       calcite, dolomite, anhydrite, illite, water, gas, props, rho_components)
print(cal_dol_anh_ill)
print(fluid)