from components.reactance import Reactance
from components.resistance import Resistance
from components.reactance import vacuum_permittivity

n = 20
lg = 0.1e-3
lm = 170
core_permittivity = 1000
# mean_length_per_turn
MLT = 14e-2

# First question
wire_length = MLT * n
area = 13.07e-5
R = Resistance(wire_length, area)

print("Winding resistance {:e} ohms".format(R.resistance))

# Second question
center_area = 18e-3 * 18e-3
side_area = 18e-3 * 9e-3
top_area = 18e-3 * 9e-3

l_vertical = 25e-3
l_horizontal = 35e-3

Rcu = Reactance(l_vertical, center_area, core_permittivity)
Rcg = Reactance(lg, center_area)
Rc = Rcu*2 + Rcg

Rsu = Reactance(l_vertical, side_area, 1000)
Rsg = Reactance(lg, side_area)
Rt = Reactance(l_horizontal, top_area, 1000)
Rs = Rsu*2 + Rsg + Rt*2

Re = Rc + Rs.parallel(Rs)
L = n**2/Re.reactance
print("Winding inductance {:e} H".format(L))

# Question 3
B_sat = 0.4
I_sat = B_sat*center_area*n/L
print("Saturation current {} A".format(I_sat))

# Question 4
F = B_sat*center_area*Rcg.reactance
print("Mangetomotiveforce of airgap {} A".format(F))
