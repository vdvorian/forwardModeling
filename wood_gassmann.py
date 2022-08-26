import math
import numpy as np

# bulk модуль смеси флюидов по формуле Вуда (prop - в процентах)
def get_fluid_modulus_by_wood(fluid1, fluid2, prop):
    # функция принимает на вход объемные модули сжатия и объемное содержание всех флюидов,
    # входящих в поронасыщающую смесь, и возвращает модуль сжатия смеси (модуль сдвига флюида всегда = 0)

    bulk = [fluid1[0], fluid2[0]]
    average_shear = 0

    if bulk[0] == 0:
        bulk[0] = 1e-7
    if bulk[1] == 0:
        bulk[1] = 1e-7

    bulk = np.array(bulk)
    prop = np.array(prop)

    new_prop = prop / 100   # объемные отношения в долях единицы
    divided_bulk = np.sum(new_prop / bulk)
    average_bulk = 1 / divided_bulk   # объемный модуль сжатия смеси флюидов

    return [average_bulk, average_shear]


# Vp в смеси флюидов по формуле Вуда (prop - в процентах)
def get_velocity_by_wood(get_bulk_modulus_by_wood, bulk, dens, prop):
    # функция принимает на вход объемные модули сжатия, значения плотностей и объемное содержание всех флюидов,
    # входящих в поронасыщающую смесь, и возвращает скорость звука в этом флюиде

    bulk = np.array(bulk)
    prop = np.array(prop)
    dens = np.array(dens)

    average_bulk = get_bulk_modulus_by_wood(bulk, prop)   # объемный модуль сжатия смеси флюидов
    new_prop = prop / 100   # объемные отношения в долях единицы
    average_dens = np.sum(new_prop * dens)   # плотность смеси флюидов

    velocity = np.sqrt(average_bulk / average_dens)

    return velocity

# формула Гассмана - получаем упругие модули породы, поры которой насыщены флюидом
def get_saturated_by_gassman(dry, matrix, fluid, porosity):
    k_dry, g_dry = dry  # сухая порода
    k_m, g_m = matrix  # твердое вещество (без пор)
    k_fl, g_fl = fluid  # флюид

    g_sat = g_dry

    k_sat = k_dry + (1 - k_dry / k_m) ** 2 / (porosity / k_fl + (1 - porosity) / k_m - k_dry / k_m ** 2)

    return [k_sat, g_sat]
