import scipy.integrate as integrate


# вспомогательная функция для integrate.solve_ivp: приготовим наши ОДУ
def prepare_ODU(t, y):
    k1, n1 = y   # начальные условия - упругие модули твердой компоненты

    p = (k1 + 4 / 3 * n1) / (k2 + 4 / 3 * n1)
    dzeta = n1 * (9 * k1 + 8 * n1) / (6 * (k1 + 2 * n1))
    q = (n1 + dzeta) / (n2 + dzeta)

    dkdt = (k2 - k1) * p / (1 - t)
    dndt = (n2 - n1) * q / (1 - t)

    return [dkdt, dndt]



def get_moduli_by_DEM(prepare_ODU, pores, matrix, porosity):
    # функция принимает на вход два массива следующего вида:
    # pores = [bulk_p, shear_p], где элементы массива: bulk и shear модули и аспектное отношение флюида,
        # насыщающего поры (воздух, например)
    # matrix = [bulk_m, shear_m]

    # porosity - пористость

    # возвращает bulk и shear модули композита матрица+поры

    k1, n1 = matrix
    k2, n2 = pores

    result = integrate.solve_ivp(fun = prepare_ODU, t_span = (0,0.999), y0 = [k1, n1],
                                 dense_output = 'true', max_step = 0.001, vectorized = 'true')

    return result.t, result.y[0], result.y[1]

