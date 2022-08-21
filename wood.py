import math
import numpy as np

# bulk модуль смеси флюидов по формуле Вуда (prop - в процентах)
def get_bulk_modulus_by_wood(bulk, prop):
    # функция принимает на вход объемные модули сжатия и объемное содержание всех флюидов,
    # входящих в поронасыщающую смесь, и возвращает модуль сжатия смеси (модуль сдвига флюида всегда = 0)

    bulk = np.array(bulk)
    prop = np.array(prop)

    new_prop = prop / 100   # объемные отношения в долях единицы
    divided_bulk = np.sum(new_prop / bulk)
    average_bulk = 1 / divided_bulk   # объемный модуль сжатия смеси флюидов

    return average_bulk


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
