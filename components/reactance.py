import math

vacuum_permittivity = 4e-7 * math.pi


class Reactance:

    def __init__(self, large, cross_section_area, relative_permittivity=1):
        permittivity = relative_permittivity * vacuum_permittivity
        self.reactance = large / (permittivity * cross_section_area)