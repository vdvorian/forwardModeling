from HS import *
from SCA import *
from DEM import *
from wood_gassmann import *
import matplotlib.pyplot as plt


# смешать кальцит и доломит по HS в пропорции 1:3
# добавить в твердое вещество поры по DEM (пористость 5%)
# смешать воду и воздух по Гассману в пропорции 1:1
# насытить флюидом поры

calcite = [71, 30]
dolomite = [80, 49]
gas = [0.04, 0]
water = [2.5, 0]

prop_calc_dol = 25
porosity = 5


matrix = get_moduli_by_HS(get_HS_for_all_proportions, calcite, dolomite, prop_calc_dol)
print('композит кальцит+доломит:', matrix)

matrix_pores = get_moduli_by_DEM(get_all_values_by_DEM, matrix, porosity)
print('кальцит+доломит с порами', matrix_pores)

fluid = get_fluid_modulus_by_wood(gas, water, prop = 3)
print('газ + вода', fluid)

final_saturated_rock = get_saturated_by_gassman(matrix_pores, matrix, fluid, porosity)
print('насыщенная флюидом порода', final_saturated_rock)