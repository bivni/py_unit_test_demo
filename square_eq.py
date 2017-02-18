# -*- coding: utf-8 -*-

import math


def solve_sqe(a, b, c):
    D = b ** 2 - 4 * a * c
    if D < 0:
        return ()
    elif D == 0:
        # если бы не было запятой был бы скаляр, а не кортеж
        return (-b / (2 * a),)

    else:
        D_root = math.sqrt(D)
        return (-b - D_root) / (2 * a), (-b + D_root) / (2 * a)
