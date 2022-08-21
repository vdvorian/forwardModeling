from DEM import *

pores = [0, 0]
matrix = [50, 10]
porosity = 10

print(get_moduli_by_DEM(prepare_ODU, pores, matrix, porosity))