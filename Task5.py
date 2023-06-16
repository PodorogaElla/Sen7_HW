import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

alpha = 0.05
data = [2.51, 2.35, 2.74, 2.56, 2.40, 2.36, 2.65, 2.7, 2.67, 2.34]
n = len(data)
mean = np.mean(data)
std = np.std(data, ddof=1)
t_stat = (mean - 2.5) / (std / np.sqrt(10))
t_critical = stats.t.ppf(1 - alpha, n - 1)
if t_stat < t_critical:
    print(
        ">>> Нулевая гипотеза не отвергается, партия изготавливается со средним арифметическим 2,5 см.")
else:
    print(
        ">>> Нулевая гипотеза отвергается, партия изготавливается со средним арифметическим не равным 2,5 см.")

print (mean, std, t_stat, t_critical)