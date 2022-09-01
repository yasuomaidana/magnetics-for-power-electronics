import math

cos = math.cos
sin = math.sin
cosh = math.cosh
sinh = math.sinh


def g1(phi):
    return (sinh(2 * phi) + sin(2 * phi)) / (cosh(2 * phi) - cos(2 * phi))


def g2(phi):
    return (sinh(phi) * cos(phi) + cosh(phi) * sin(phi)) / (cosh(2 * phi) - cos(2 * phi))


def m(f_0, f_h):
    if f_0 - f_h > 0:
        return f_0 / (f_0 - f_h)
    return f_h / (f_h - f_0)

