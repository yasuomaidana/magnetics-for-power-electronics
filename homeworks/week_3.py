import math

def calculate_error(real,calculated):
    return math.fabs((real-calculated)/real*100) 

P_out = 150.0
V_out = 48.0
Vg = 28.0
fs = 100.0e3
delta_i_percentage = 0.10

i_out = P_out/V_out

D = 1 - Vg/V_out
D_p = 1-D

i_in = 1/D_p*i_out

delta_i = i_in*delta_i_percentage


print("D: {:.3f} D'{:.3f}".format(D,D_p))
print("Io {} Iin {}".format(i_out,i_in))


Lc = D*Vg/(2*fs*delta_i)

L = 108.889e-6
print("First answer")
print("Inductance L= {:e}, calculated {:e}, error {:.2f}%".format(L,Lc,calculate_error(L,Lc)))

Pcu = 0.75

R = Pcu*(D_p/i_out)**2
print("Second answer")
print("Resistance R={:e}, calculated {:e}, error {:.2f}".format(0.02613333,R,calculate_error(0.02613333,R)))
