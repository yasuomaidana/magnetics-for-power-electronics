from components.reactance import Reactance
from components.resistance import Resistance
import numpy as np

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
Rc = Rcu * 2 + Rcg

Rsu = Reactance(l_vertical, side_area, 1000)
Rsg = Reactance(lg, side_area)
Rt = Reactance(l_horizontal, top_area, 1000)
Rs = Rsu * 2 + Rsg + Rt * 2

Re = Rc + Rs.parallel(Rs)
L = n ** 2 / Re.reactance
print("Winding inductance {:e} H".format(L))

# Question 3
B_sat = 0.4
I_sat = B_sat * center_area * n / L
print("Saturation current {} A".format(I_sat))

# Question 4
F = B_sat * center_area * Rcg.reactance
print("Mangetomotiveforce of airgap {} A".format(F))

# Questions 5 and 6
# power_loss = Kfe * B_max ^ beta
# ln(power_loss) = ln(Kfe) + beta * ln(B_max)
# ln(Kfe) = x
# ln(power_loss) = x + beta * ln(B_max)
# A * X = B
# X = [x , y]
# B = [ln(power_loss1),ln(power_loss2)]
# A = [[1,ln(B_max1)],[1,ln(B_max2)]]


loss_1 = 0.2
B_max_1 = 0.1
loss_2 = 0.01
B_max_2 = 0.04

nl_B_max_1 = np.log(B_max_1)
nl_B_max_2 = np.log(B_max_2)
nl_loss1 = np.log(loss_1)
nl_loss2 = np.log(loss_2)

A = np.array([[1, nl_B_max_1], [1, nl_B_max_2]])
B = np.array([nl_loss1, nl_loss2])
[x, Beta] = np.linalg.inv(A).dot(B)
Kfe = np.exp(x)
print("Kfe: {} Beta: {}".format(Kfe, Beta))

