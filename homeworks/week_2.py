def power_ratio(f_0, f_h):
    return f_0 ** 2 + f_h ** 2


def calculate_total_power_ratio(levels):
    fs = [(levels[i], levels[i + 1]) for i in range(len(levels)-1)]
    factors = [power_ratio(f0, fh) for f0, fh in fs]
    print("ranges {}".format(fs))
    print("total power {}P".format(sum(factors)))


calculate_total_power_ratio([0, 2, 1, 0, -1, -2, 0])
calculate_total_power_ratio([0, -1, 1, 0, -1, 1, 0])
