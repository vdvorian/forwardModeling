from SCA import *
from DEM import *

pores = [1, 1, 1]
matrix = [50, 10, 1]
porosity = 10

pores_dem = [1, 1]
matrix_dem = [50, 10]

por, kbr, nbr = get_all_values_by_SCA(pores, matrix)
print(por)
print(kbr)
print(nbr)

print(get_moduli_by_SCA(get_all_values_by_SCA, pores, matrix, porosity))


por_dem, kdem, ndem = get_all_values_by_DEM(pores_dem, matrix_dem)

