from components.reactance import Reactance
from components.resistance import Resistance

n = 20
lg = 0.1e-3
#mean_length_per_turn
MLT = 14e-2

wire_length = MLT*n
area = 13.07e-5

R = Resistance(wire_length, area)

print("Winding resistance {:e} ohms".format(R.resistance))

R1 = Reactance(9e-2, 1e-2, 1000)
print(R1.reactance)
