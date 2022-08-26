from HS import *
from SCA import *
from DEM import *
from wood_gassmann import *

import matplotlib.pyplot as plt
from time import time
from math import *


# 40% кальцита, 30% доломита, 15% ангидрита, 10% иллита, 5% пор: 4 круглых пор и 1 трещин

calcite = [70.8, 30.3]
dolomite = [80.2, 48.8]
anhydrite = [59.1, 31.4]
illite = [25.3, 16.3]

gas = [0.041, 0]
water = [2.496, 0]

cal_proportion = 40
dol_proportion = 30
anh_proportion = 15
ill_proportion = 10

porosity = 5


# кальцит и доломит по Хашину-Штрикману
proportion = round(get_proportion_for_HS(cal_proportion, dol_proportion))
cal_dol = get_moduli_by_HS(get_HS_for_all_proportions, calcite, dolomite, proportion)
print('HS кальцит + доломит:', cal_dol)

# кальцит, доломит и ангидрит по Хашину-Штрикману
proportion = round(get_proportion_for_HS(anh_proportion, cal_proportion + dol_proportion))
cal_dol_anh = get_moduli_by_HS(get_HS_for_all_proportions, anhydrite, cal_dol, proportion)
print('HS кальцит + доломит + ангидрит:', cal_dol_anh)

# кальцит, доломит, ангидрит + иллит по SCA
proportion = round(get_proportion_for_HS(ill_proportion, cal_proportion + dol_proportion + anh_proportion))
cal_dol_anh_ill = get_moduli_by_SCA(get_all_values_by_SCA, [25.3, 16.3, 0.001],
                                    [cal_dol_anh[0], cal_dol_anh[1], 1], proportion)
print('SCA (кальцит + доломит + ангидрит) + иллит:', cal_dol_anh_ill)

# круглые поры в твердую матрицу по DEM
matrix_pores = get_moduli_by_DEM(get_all_values_by_DEM, cal_dol_anh_ill, 4)
print('DEM твердая матрица + круглые поры (воздух):', matrix_pores)

# трещины в матрицу с порами по SCA
matrix_cracks = get_moduli_by_SCA(get_all_values_by_SCA, [0, 0, 0.01],
                                    [matrix_pores[0], matrix_pores[1], 1], 1)
print('SCA твердая матрица с порами + трещины:', matrix_cracks)
print()

# упругие модули флюида по Вуду
fluid = get_fluid_modulus_by_wood(gas, water, 50)
print('Wood: упругие модули флюида:', fluid)

# насытим поры флюидом
saturated = get_saturated_by_gassman(matrix_cracks, cal_dol_anh_ill, fluid, 5)
print('Gassmann: готовая порода:', saturated)


rho = 2.87
k, g = saturated[0], saturated[1]

vp = sqrt((k + g * 4/3) / rho)
vs = sqrt(g / rho)

print('vp', vp, 'км/c')
print('vs', vs, 'км/c')
