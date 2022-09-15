import math

from components.resistance import resistance_dc


def power_ratio(f_0, f_h):
    return f_0 ** 2 + f_h ** 2


def calculate_total_power_ratio(levels):
    fs = [(levels[i], levels[i + 1]) for i in range(len(levels) - 1)]
    factors = [power_ratio(f0, fh) for f0, fh in fs]
    print("ranges {}".format(fs))
    print("total power {}P".format(sum(factors)))


# Question 7
calculate_total_power_ratio([0, 2, 1, 0, -1, -2, 0])
# Question 8
calculate_total_power_ratio([0, -1, 1, 0, -1, 1, 0])

# Question 9
width = 0.780e-2
thickness = 0.343e-3
nu = 1
MLT = 4.40e-2
d = math.sqrt(4/math.pi)*thickness
print(d)
nl = nu * width * math.sqrt(4 / math.pi) / d
print(nl)
n = 5.5
ro = 2.3e-8
resistance = resistance_dc(ro, MLT, n, nu, width)
r = ro * MLT * 1 ** 3 / (nu * width ** 2)
print(r)
print("resistance {:e}".format(resistance.resistance))
print(math.pow(2.6478e-3/r, 1 / 3))
