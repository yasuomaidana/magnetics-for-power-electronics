ro = {"cuS": 1.724e-6, "cu100": 2.34e-6}


class Resistance:
    def __init__(self, length, cross_section_area, ro_value=ro["cuS"]):
        self.value = ro_value * length / cross_section_area

    def loss(self, rms_current):
        return self.value * rms_current ** 2
