import math

vacuum_permittivity = 4e-7 * math.pi


class Reactance:

    def __init__(self, large, cross_section_area, relative_permittivity=1):
        permittivity = relative_permittivity * vacuum_permittivity
        self.reactance = large / (permittivity * cross_section_area)

    def __add__(self, other):
        new_reactance = Reactance(1, 1)
        new_reactance.reactance = self.reactance + other.reactance
        return new_reactance

    def parallel(self, other):
        new_reactance = Reactance(1, 1)
        new_reactance.reactance = 1/(1/self.reactance + 1/other.reactance)
        return new_reactance

    def __mul__(self, other):
        new_reactance = Reactance(1, 1)
        if other is Reactance:
            new_reactance.reactance = self.reactance * other.reactance
        else:
            new_reactance.reactance = self.reactance * other
        return new_reactance
