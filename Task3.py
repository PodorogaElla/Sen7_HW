import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

alpha=0.05
x1=np.array([150, 160, 165, 145, 155])
x2=np.array([140, 155, 150, 130, 135])
d = stats.wilcoxon(x1, x2)
print('\n>>> Statistics = %.2f \n>>> Р-value = %.3f' % (d))
s, p = stats.wilcoxon(x1, x2)
if p > alpha:
    print('>>> Cтатистически значимых различий нет, нулевая гипотеза'
          ' не отвергается, препарат не влияет на давление.')
else:
    print('>>> Cтатистически значимые различия присутствуют, нулевую '
          'гипотезу отвергаем, препарат влияет на давление.')