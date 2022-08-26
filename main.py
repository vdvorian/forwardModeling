from HS import *
from SCA import *
from DEM import *
from wood_gassmann import *

import matplotlib.pyplot as plt
from time import time



calcite = [70.8, 30.3]
dolomite = [80.2, 48.8]
anhydrite = [59.1, 31.4]
illite = [25.3, 16.3]

gas = [0.041, 0]
water = [2.496, 0]


# смешаем кальцит и доломит по Хашину-Штрикману в пропорции 1:1
proportion = 50
dol_prop, dol_bulk_d, dol_bulk_u, dol_shear_d, dol_shear_u = get_HS_for_all_proportions(calcite, dolomite)

dol_bulk_average = []
dol_shear_average = []
for i in range(len(dol_prop)):
    dol_bulk_average.append((dol_bulk_d[i] + dol_bulk_u[i])/2)
    dol_shear_average.append((dol_shear_d[i] + dol_shear_u[i])/2)


print(dol_prop)
print(dol_bulk_average)
print(dol_bulk_d)
print(dol_bulk_u)

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(3, 3))
fig.suptitle('Calcite + Dolomite (HS)')

axes[0].plot(dol_prop, dol_bulk_d, c = 'b')
axes[0].plot(dol_prop, dol_bulk_u, c = 'r')
axes[0].plot(dol_prop, dol_bulk_average, c = 'k')
axes[0].scatter(dol_prop[proportion], dol_bulk_average[proportion], c = 'k')
axes[0].set_title('Bulk Modulus')

axes[1].plot(dol_prop, dol_shear_d, c = 'b')
axes[1].plot(dol_prop, dol_shear_u, c = 'r')
axes[1].plot(dol_prop, dol_bulk_average, c = 'k')
axes[1].scatter(dol_prop[proportion], dol_shear_average[proportion], c = 'k')
axes[1].set_title('Shear Modulus')

axes[0].show()




