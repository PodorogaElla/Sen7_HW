import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

alpha=0.05
x1=np.array([150, 160, 165, 145, 155])
x2=np.array([140, 155, 150, 130, 135])
x3=np.array([130, 130, 120, 130, 125])
d = stats.friedmanchisquare(x1, x2, x3)
print('\n>>> Statistics = %.2f \n>>> Р-value = %.3f' % (d))
s, p = stats.friedmanchisquare(x1, x2, x3)
if p > alpha:
    print('>>> Cтатистически значимых различий нет, нулевая гипотеза не отвергается, '
          'препарат не влияет на давление.')
else:
    print('>>> Cтатистически значимые различия присутствуют, нулевую '
          'гипотезу отвергаем, препарат влияет на давление.')