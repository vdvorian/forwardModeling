from HS import *
from SCA import *
from DEM import *
from wood_gassmann import *

import matplotlib.pyplot as plt
from time import time
from math import *



def do_forward_problem(get_proportion_for_HS, get_moduli_by_HS, get_moduli_by_SCA, get_moduli_by_DEM,
                       get_fluid_modulus_by_wood, get_saturated_by_gassman, get_velocity,
                       calcite, dolomite, anhydrite, illite, water, gas, props, rho_components):

    cal_prop, dol_prop, anh_prop, ill_prop, porosity = props[0], props[1], props[2], props[3], props[4]

    start = time()

    # кальцит и доломит по Хашину-Штрикману
    proportion = round(get_proportion_for_HS(cal_prop, dol_prop))
    cal_dol = get_moduli_by_HS(get_HS_for_all_proportions, calcite, dolomite, proportion)

    # кальцит, доломит и ангидрит по Хашину-Штрикману
    proportion = round(get_proportion_for_HS(anh_prop, cal_prop + dol_prop))
    cal_dol_anh = get_moduli_by_HS(get_HS_for_all_proportions, anhydrite, cal_dol, proportion)

    # кальцит, доломит, ангидрит + иллит по SCA
    proportion = round(get_proportion_for_HS(ill_prop, cal_prop + dol_prop + anh_prop))
    cal_dol_anh_ill = get_moduli_by_SCA(get_all_values_by_SCA, [illite[0], illite[1], 0.001],
                                        [cal_dol_anh[0], cal_dol_anh[1], 1], proportion)

    # круглые поры в твердую матрицу по DEM
    matrix_pores = get_moduli_by_DEM(get_all_values_by_DEM, cal_dol_anh_ill, porosity)

    # упругие модули флюида по Вуду
    fluid = get_fluid_modulus_by_wood(gas, water, 50)

    # насытим поры флюидом
    saturated = get_saturated_by_gassman(matrix_pores, cal_dol_anh_ill, fluid, porosity)

    # рассчитаем скорости Vp и Vs
    vp, vs = get_velocity(rho_components, props, saturated)

    end = time()

    return vp, vs, end - start



def do_forward_problem_matrix(get_proportion_for_HS, get_moduli_by_HS, get_moduli_by_SCA, get_moduli_by_DEM,
                       get_fluid_modulus_by_wood, get_saturated_by_gassman, get_velocity,
                       calcite, dolomite, anhydrite, illite, water, gas, props, rho_components):

    cal_prop, dol_prop, anh_prop, ill_prop, porosity = props[0], props[1], props[2], props[3], props[4]

    start = time()

    # кальцит и доломит по Хашину-Штрикману
    proportion = round(get_proportion_for_HS(cal_prop, dol_prop))
    cal_dol = get_moduli_by_HS(get_HS_for_all_proportions, calcite, dolomite, proportion)

    # кальцит, доломит и ангидрит по Хашину-Штрикману
    proportion = round(get_proportion_for_HS(anh_prop, cal_prop + dol_prop))
    cal_dol_anh = get_moduli_by_HS(get_HS_for_all_proportions, anhydrite, cal_dol, proportion)

    # кальцит, доломит, ангидрит + иллит по SCA
    proportion = round(get_proportion_for_HS(ill_prop, cal_prop + dol_prop + anh_prop))
    cal_dol_anh_ill = get_moduli_by_SCA(get_all_values_by_SCA, [illite[0], illite[1], 0.001],
                                        [cal_dol_anh[0], cal_dol_anh[1], 1], proportion)

    # упругие модули флюида по Вуду
    fluid = get_fluid_modulus_by_wood(gas, water, 50)

    return cal_dol_anh_ill, fluid


def do_forward_problem_pores(do_forward_problem_matrix, get_proportion_for_HS, get_moduli_by_HS, get_moduli_by_SCA,
                             get_moduli_by_DEM, get_fluid_modulus_by_wood, get_saturated_by_gassman, get_velocity,
                             calcite, dolomite, anhydrite, illite, water, gas, props, rho_components):

    cal_dol_anh_ill, fluid = do_forward_problem_matrix(get_proportion_for_HS, get_moduli_by_HS, get_moduli_by_SCA,
                                                get_moduli_by_DEM, get_fluid_modulus_by_wood, get_saturated_by_gassman,
                                                get_velocity, calcite, dolomite, anhydrite, illite, water, gas, props,
                                                rho_components)


    # круглые поры в твердую матрицу по DEM
    matrix_pores = get_moduli_by_DEM(get_all_values_by_DEM, cal_dol_anh_ill, porosity)

    # упругие модули флюида по Вуду
    fluid = get_fluid_modulus_by_wood(gas, water, 50)

    # насытим поры флюидом
    saturated = get_saturated_by_gassman(matrix_pores, cal_dol_anh_ill, fluid, porosity)

    # рассчитаем скорости Vp и Vs
    vp, vs = get_velocity(rho_components, props, saturated)

    end = time()

    return vp, vs, end - start