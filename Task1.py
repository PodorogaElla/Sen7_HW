import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

alpha = 0.05
x= np.array([380, 420, 290])
y= np.array([140, 360, 200, 900])
d = stats.mannwhitneyu(x,y)
print('\n>>> Statistics = %.2f \n>>> Р-value = %.3f' % (d))
s, p = stats.mannwhitneyu(x,y)
if p > alpha:
    print('>>> Cтатистически значимых различий нет, нулевая гипотеза не отвергается.')
else:
    print('>>> Cтатистически значимые различия присутствуют, нулевую гипотезу отвергаем.')