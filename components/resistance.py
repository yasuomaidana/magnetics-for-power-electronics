ro = {"cuS": 1.724e-6, "cu100": 2.34e-6}


def resistance_dc(ro_value, mlt, nl, nu, lw):
    return Resistance(mlt * nl ** 3, nu * lw ** 2, ro_value)


class Resistance:
    def __init__(self, length, cross_section_area, ro_value=ro["cuS"]):
        self.resistance = ro_value * length / cross_section_area

    def loss(self, rms_current):
        return self.resistance * rms_current ** 2
